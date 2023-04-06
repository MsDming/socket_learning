from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QVBoxLayout, QLabel, QHBoxLayout


class User:
    def __init__(self, account, passwd, nickName):
        self.account = account
        self.passwd = passwd
        self.nickName = nickName


class Channel:
    def __init__(self, channelIndex, channelName: str):
        self.channelIndex = str(channelIndex)
        self.channelName = channelName

    def to_dict_str(self):
        return {
            'channelIndex':self.channelIndex,
            'channelName':self.channelName
        }


class Channel_QListWidgetItem(QListWidgetItem):
    def __init__(self, channel: Channel):
        super().__init__()
        self.channel = channel
        self.widget = QWidget()
        hbox = QHBoxLayout()
        lb_channelIcon = QLabel()
        lb_channelIcon.setPixmap(QPixmap('D:\\Study\\计算机网络\\socket_learning\\client\\images\\test.jpg',).scaled(40, 40))
        lb_channelName = QLabel(self.channel.channelName)
        hbox.addWidget(lb_channelIcon)
        hbox.addWidget(lb_channelName)
        self.widget.setLayout(hbox)
        self.setSizeHint(self.widget.sizeHint())
