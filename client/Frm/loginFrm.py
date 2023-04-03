import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QApplication, QWidget
from client.Frm.hallFrm import HallFrm
from client.ui_py.ui_login import Ui_login
from client.utils.model import User


class LoginMw(QWidget, Ui_login):
    signalUser = pyqtSignal(User)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connect_signals_slots()
        self.show()

    def initSocket(self):
        self.tcpSkt = QTcpSocket(self)
        self.tcpSkt.connectToHost('localhost', 5000)

    def connect_signals_slots(self):
        self.pushButton_login.clicked.connect(self.login)
        self.pushButton_register.clicked.connect(self.register)
        # self.signalUser.connect(HallFrm.get_user_from_parent)

    def login(self):
        self.label_loginFailed.setText("")
        account = self.lineEdit_account.text()
        passwd = self.lineEdit_password.text()
        print("input account={}".format(account))
        print("input passwd={}".format(passwd))

        if (account, passwd) == ('root', '111111'):
            global hallWindow
            hallWindow = HallFrm()
            self.signalUser.connect(hallWindow.get_user_from_parent)
            self.signalUser.emit(User('root', '111111', 'nickname'))
            hallWindow.show()
            self.close()
        else:
            self.label_loginFailed.setText("账户或密码输入错误，请重试")

    def register(self):
        pass


if __name__ == '__main__':
    IP = "localhost"
    PORT = 5000
    ADDR = (IP, PORT)
    app = QApplication(sys.argv)
    loginMw = LoginMw()
    app.exec()
