import sys
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from client.ui_py.ui_hall import Ui_hall
import ast

from client.utils.model import Channel, Channel_QListWidgetItem


class HallFrm(QMainWindow, Ui_hall):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listWidget_channels.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget_channels.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.channelList = None
        self.tcpSkt = None
        self.user = None
        self.setupUi(self)
        self.tcpSkt = QTcpSocket(parent=self)
        self.tcpSkt.connectToHost('localhost', 5000)
        data = {'type': 'channels'}
        data = data.__str__()
        self.tcpSkt.write(data.encode('utf-8'))
        self.tcpSkt.readyRead.connect(self.read_channels_from_server)

    def init_channel_view(self):
        for i in self.channelList:
            item = Channel_QListWidgetItem(Channel(i['channelIndex'], i['channelName']))
            self.listWidget_channels.addItem(item)
            self.listWidget_channels.setItemWidget(item, item.widget)

    def get_user_from_parent(self, user):
        self.user = user
        self.setWindowTitle(self.user.nickName)

    def read_channels_from_server(self):
        recvData = self.tcpSkt.read(1024).decode('utf-8')
        recvData = ast.literal_eval(recvData)
        self.channelList = recvData
        # self.tcpSkt.disconnectFromHost()
        self.init_channel_view()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hallFrm = HallFrm()
    hallFrm.show()
    app.exec()
