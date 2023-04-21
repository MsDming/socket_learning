import ast
import sys

import qdarkstyle
from qdarkstyle import LightPalette

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from PyQt5.QtWidgets import QApplication, QWidget
from ui_py import ui_login
from utils import models
from windows.hallWindow import HallFrm


class LoginMw(QWidget, ui_login.Ui_login):
    signalUser = pyqtSignal(models.User)

    def __init__(self):
        super().__init__()
        self.tcpSkt = None
        self.setupUi(self)
        self.tcpSkt = QTcpSocket(self)
        self.tcpSkt.connectToHost(QHostAddress('10.81.29.253'), 5000)
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_register.clicked.connect(self.register)
        self.show()

    def login(self):
        self.label_loginFailed.setText("")
        account = self.lineEdit_account.text()
        password = self.lineEdit_password.text()
        loginRequest = {"type": "login", "account": account, "password": password}.__str__()
        self.tcpSkt.write(loginRequest.encode('utf-8'))  # 发起登录请求
        self.tcpSkt.waitForReadyRead()
        loginResponse = ast.literal_eval(self.tcpSkt.read(1024).decode('utf-8'))
        loginSuccess = loginResponse["loginSuccess"]
        assert type(loginSuccess) == bool
        if loginSuccess:
            global hallWindow
            hallWindow = HallFrm()
            self.signalUser.connect(hallWindow.get_user_from_parent)
            self.signalUser.emit(models.User(account, password, loginResponse["nickname"]))  # 把User信息传递给子页面
            hallWindow.show()
            self.tcpSkt.disconnectFromHost()
            self.close()
            self.deleteLater()
        else:
            self.label_loginFailed.setText("账户或密码输入错误，请重试")

    def register(self):
        pass


if __name__ == '__main__':
    BUFF_SIZE = 1024 * 1024
    IP = "localhost"
    PORT = 5000
    ADDR = (IP, PORT)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
    loginMw = LoginMw()
    app.exec()
