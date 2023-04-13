import sys
sys.path.append(r'D:\Study\计算机网络\socket_learning')
from PyQt5.QtCore import pyqtSignal, QThreadPool
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QApplication, QMainWindow, QAbstractItemView
from client.ui_py.ui_hall import Ui_hall
import ast

from client.utils.models import Channel, Channel_QListWidgetItem, User
from client.windows.chatWindow import ChatWindow


class HallFrm(QMainWindow, Ui_hall):
    signalUser = pyqtSignal(User)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.listWidget_channels.setSelectionMode(QAbstractItemView.SingleSelection)
        self.listWidget_channels.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.channelList = []
        self.tcpSkt = None
        self.user = None
        self.setupUi(self)
        self.tcpSkt = QTcpSocket(parent=self)
        self.tcpSkt.connectToHost('localhost', 5000)
        data = {'type': 'channels'}
        data = data.__str__()
        self.tcpSkt.write(data.encode('utf-8'))
        print('发送获取channels请求')
        self.tcpSkt.waitForReadyRead()
        self.get_channels_from_server()
        self.listWidget_channels.itemDoubleClicked.connect(self.open_chat_window)
        self.chatWindowsList = [None for i in range(len(self.channelList) + 1)]

    def init_channel_view(self):
        for i in self.channelList:
            item = Channel_QListWidgetItem(Channel(i['channelIndex'], i['channelName']))
            self.listWidget_channels.addItem(item)
            self.listWidget_channels.setItemWidget(item, item.widget)

    def get_user_from_parent(self, user: User):
        self.user = user
        self.setWindowTitle(self.user.nickname)

    def get_channels_from_server(self):
        recvData = self.tcpSkt.read(1024).decode('utf-8')
        recvData = ast.literal_eval(recvData)
        self.channelList = recvData
        self.init_channel_view()
        self.tcpSkt.disconnectFromHost()

    def open_chat_window(self):

        if self.chatWindowsList[self.listWidget_channels.selectedItems()[0].channel.channelIndex] is not None:
            self.chatWindowsList[self.listWidget_channels.selectedItems()[0].channel.channelIndex].show()
            self.chatWindowsList[self.listWidget_channels.selectedItems()[0].channel.channelIndex].activateWindow()
            return
        channel = self.listWidget_channels.selectedItems()[0].channel
        assert type(channel) == Channel
        print("Channel:{}".format(channel.to_dict()))
        chatWindow = ChatWindow(channel)
        self.signalUser.connect(chatWindow.get_user_from_parent)
        self.signalUser.emit(self.user)
        assert type(channel.channelIndex) == int
        self.chatWindowsList[channel.channelIndex] = chatWindow
        chatWindow.show()

    def dispose_chat_window(self):
        chatWindow = self.sender()
        if chatWindow in self.chatWindowsList:
            self.chatWindowsList.remove(chatWindow)
            print("删除页面")

    def closeEvent(self, a0: QCloseEvent) -> None:
        del self.chatWindowsList
        self.tcpSkt.deleteLater()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hallFrm = HallFrm()

    hallFrm.show()
    app.exec()
