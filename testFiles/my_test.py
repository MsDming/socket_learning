import ast
import sys

from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QWidget, QApplication


class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.tcpSkt = QTcpSocket(self)
        self.tcpSkt.connectToHost('localhost', 5000)
        self.tcpSkt.readyRead.connect(self.recv_test)
        data = {'type': 'channels'}
        data = data.__str__()
        self.tcpSkt.write(data.encode('utf-8'))

    def recv_test(self):
        print("recvFuc")
        recvData = self.tcpSkt.read(1024).decode('utf-8')
        recvData = ast.literal_eval(recvData)
        print(recvData)
        print(type(recvData))

    def __del__(self):
        self.tcpSkt.close()


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # testWidget = TestWidget()
    #
    # app.exec()
    test = {'loginSuccess': True, 'nickName': '飞翔的企鹅'}.__str__()
    print(type(test))
    test=ast.literal_eval(test)
    print(test['loginSuccess'])
    print(type(test['loginSuccess']))
