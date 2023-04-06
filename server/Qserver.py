import sys

from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtNetwork import QTcpServer, QHostAddress, QTcpSocket


class MyServer(QWidget):
    def __init__(self):
        super().__init__()
        self.clients = []
        self.server = QTcpServer(self)
        self.server.setMaxPendingConnections(100)
        self.server.newConnection.connect(self.incomingConnection)

    def start_server(self):
        if not self.server.listen('localhost', 5000):
            print("Could not start server")
            return False

        print("Server started on port", 5000)
        return True

    def incomingConnection(self, socketDescriptor):
        client = QTcpSocket(self)
        client.setSocketDescriptor(socketDescriptor)
        self.clients.append(client)
        print("New client connected from{}:{}".format(client.peerAddress(), client.peerPort()))

        thread = QThread(self)
        client.moveToThread(thread)
        client.readyRead.connect(lambda: self.recv_msg(client))
        client.disconnected.connect(thread.quit)
        thread.finished.connect(client.deleteLater)
        thread.start()

    def recv_msg(self, client: QTcpSocket):
        msg = client.read(1024).decode('utf-8')
        # TODO: process msg


if __name__ == '__main__':
    app = QApplication(sys.argv)
    server = MyServer()
    server.start_server()
    app.exec()
