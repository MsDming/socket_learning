from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QListWidgetItem, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QTextBrowser


class User:
    def __init__(self, account, passwd, nickname):
        self.account = account
        self.password = passwd
        self.nickname = nickname


class Channel:
    def __init__(self, channelIndex, channelName: str):
        self.channelIndex = int(channelIndex)
        self.channelName = channelName

    def to_dict(self):
        return {
            'channelIndex': self.channelIndex,
            'channelName': self.channelName
        }


class Channel_QListWidgetItem(QListWidgetItem):
    def __init__(self, channel: Channel):
        super().__init__()
        self.channel = channel
        self.widget = QWidget()
        hbox = QHBoxLayout()
        lb_channelIcon = QLabel()
        lb_channelIcon.setPixmap(
            QPixmap('D:\\Study\\计算机网络\\socket_learning\\client\\images\\test.jpg').scaled(40, 40))
        lb_channelName = QLabel(self.channel.channelName)
        hbox.addWidget(lb_channelIcon)
        hbox.addWidget(lb_channelName)
        self.widget.setLayout(hbox)
        self.setSizeHint(self.widget.sizeHint())


class html_QListWidgetItem(QListWidgetItem):
    def __init__(self, htmlMsg: str):
        super().__init__()
        self.widget = QWidget(self)
        vbox = QVBoxLayout()
        textBrowser = QTextBrowser(self.widget)
        textBrowser.textCursor().insertHtml(htmlMsg)
        vbox.addWidget(textBrowser)
        self.widget.setLayout(vbox)
        self.setSizeHint(self.widget.sizeHint())
