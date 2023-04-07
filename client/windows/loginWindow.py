import ast
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QApplication, QWidget
from client.windows.hallWindow import HallFrm
from client.ui_py.ui_login import Ui_login
from client.utils.model import User


class LoginMw(QWidget, Ui_login):
    signalUser = pyqtSignal(User)

    def __init__(self):
        super().__init__()
        self.tcpSkt = None
        self.setupUi(self)
        self.tcpSkt = QTcpSocket(self)
        self.tcpSkt.connectToHost('localhost', 5000)
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_register.clicked.connect(self.register)
        self.show()

    def login(self):
        self.label_loginFailed.clear()
        account = self.lineEdit_account.text()
        password = self.lineEdit_password.text()
        print("input account={}".format(account))
        print("input passwd={}".format(password))
        loginRequest = {"type": "login", "account": account, "password": password}.__str__()
        self.tcpSkt.write(loginRequest.encode('utf-8'))
        self.tcpSkt.waitForReadyRead()
        loginResponse = ast.literal_eval(self.tcpSkt.read(1024).decode('utf-8'))
        loginSuccess = loginResponse["loginSuccess"]
        assert type(loginSuccess) == bool
        if loginSuccess:
            global hallWindow
            hallWindow = HallFrm()
            self.signalUser.connect(hallWindow.get_user_from_parent)
            self.signalUser.emit(User(account, password, loginResponse["nickname"]))
            hallWindow.show()
            self.tcpSkt.close()
            self.close()
        else:
            self.label_loginFailed.setText("账户或密码输入错误，请重试")

    def register(self):
        pass

    def __del__(self):
        self.tcpSkt.close()
        super().__del__()


if __name__ == '__main__':
    IP = "localhost"
    PORT = 5000
    ADDR = (IP, PORT)
    app = QApplication(sys.argv)
    loginMw = LoginMw()
    app.exec()
