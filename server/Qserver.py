import ast
import sys

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtNetwork import QTcpServer, QHostAddress, QTcpSocket

from client.utils.model import Channel


class MyServer(QTcpServer):
    def __init__(self):
        super().__init__()
        self.clients = []
        self.listen(QHostAddress.LocalHost, port=5000)

    def incomingConnection(self, socketDescriptor):
        try:
            client = MyTcpSocket()
            client.setSocketDescriptor(socketDescriptor)
            self.clients.append(client)
            print("New client connected from {}:{}".format(client.peerAddress().toString(), client.peerPort()))
            thread = QThread(self)
            client.readyRead.connect(lambda: self.recv_handle_msg(client))
            thread.finished.connect(client.deleteLater)
            client.moveToThread(thread)
            thread.start()
        except Exception as e:
            print(e)

    def recv_handle_msg(self, client: QTcpSocket):
        try:
            msg = client.read(1024).decode('utf-8')
            requestDict = ast.literal_eval(msg)
            assert type(requestDict) == dict
            requestType = requestDict["type"]
            if requestType == 'channels':  # 获取频道列表请求
                res = [Channel(0, '频道1').to_dict_str(), Channel(0, '频道2').to_dict_str()]
                self.request.sendall(res.__str__().encode('utf-8'))
            elif requestType == 'login':  # 登录请求
                account, password = requestDict['account'], requestDict['password']
                if (account, password) == ('root', '111111'):
                    self.request.sendall({'loginSuccess': True, 'nickName': '飞翔的企鹅'}.__str__().encode('utf-8'))
                else:
                    self.request.sendall({'loginSuccess': False}.__str__().encode('utf-8'))
        except Exception as e:
            print(e)


class MyTcpSocket(QTcpSocket):
    def __init__(self):
        super().__init__()

    def disconnectNotify(self) -> None:
        print("Disconnected from {}:{}".format(self.peerAddress(), self.peerPort()))
        super().disconnectNotify()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    server = MyServer()
    app.exec()
