import sys

from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QApplication, QMainWindow
from client.ui_py.ui_hall import Ui_hall
import ast
import socket


class HallFrm(QMainWindow, Ui_hall):
    def __init__(self):
        super().__init__()
        self.tcpSkt = None
        self.user = None
        self.setupUi(self)
        self.tcpSkt = QTcpSocket(parent=self)
        self.tcpSkt.connectToHost('localhost', 5000)
        data = {'type': 'channels'}
        data = data.__str__()
        self.tcpSkt.write(data.encode('utf-8'))
        self.tcpSkt.readyRead.connect(self.read_channels_from_server)

    def get_user_from_parent(self, user):
        self.user = user
        self.setWindowTitle(self.user.nickName)

    def read_channels_from_server(self):
        recvData = self.tcpSkt.read(1024).decode('utf-8')
        recvData = ast.literal_eval(recvData)
        print(type(recvData))
        print(recvData)
        # self.tcpSkt.close()

    # def __del__(self):
    #     self.tcpSkt.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hallFrm = HallFrm()
    hallFrm.show()
    app.exec()
