import sys
from ast import literal_eval
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtNetwork import QTcpSocket, QHostAddress
from PyQt5.QtWidgets import QWidget
from pathlib import Path

FILE = Path(__file__).resolve()
ROOT = FILE.parents[2]
sys.path.append(str(ROOT))
from client.windows.registerWindow import RegisterMw
from client.ui_py.ui_login import Ui_login
from client.utils import models
from client.windows.hallWindow import HallFrm


class LoginMw(QWidget, Ui_login):
    signalUser = pyqtSignal(models.User)

    def __init__(self):
        super().__init__()
        self.tcpSkt = None
        self.setupUi(self)
        self.tcpSkt = QTcpSocket(self)
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_register.clicked.connect(self.register)
        self.lineEdit_IP.setText("127.0.0.1")
        self.show()

    def login(self):
        try:
            self.tcpSkt.connectToHost(QHostAddress(f'{self.lineEdit_IP.text()}'), 5000)
        except Exception as e:
            print(e)
            self.label_loginFailed.setText("服务器连接失败，请重试")
            return
        self.label_loginFailed.setText("")
        account = self.lineEdit_account.text()
        password = self.lineEdit_password.text()
        loginRequest = {"type": "login", "account": account, "password": password}.__str__()
        self.tcpSkt.write(loginRequest.encode('utf-8'))  # 发起登录请求
        self.tcpSkt.waitForReadyRead()
        loginResponse = literal_eval(self.tcpSkt.read(1024).decode('utf-8'))
        loginSuccess = loginResponse["loginSuccess"]
        assert type(loginSuccess) == bool
        if loginSuccess:
            global hallWindow
            hallWindow = HallFrm(self.lineEdit_IP.text())
            self.signalUser.connect(hallWindow.get_user_from_parent)
            self.signalUser.emit(models.User(account, password, loginResponse["nickname"]))  # 把User信息传递给子页面
            hallWindow.show()
            self.tcpSkt.disconnectFromHost()
            self.close()
            self.deleteLater()
        else:
            self.label_loginFailed.setText("账户或密码输入错误，请重试")

    def register(self):
        return
        self.registerWidget = RegisterMw(IP=self.ip)
