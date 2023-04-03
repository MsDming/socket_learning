import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QApplication, QListView
from client.utils.model import Channel



class TestWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 300)
        print(1)
        self.listView = QListView()
        dataLs = [Channel(1, '频道1'), Channel(2, '频道2')]
        channelLsMd = ListModelChannel(dataLs)
        self.listView.setModel(channelLsMd)
        vLayout = QVBoxLayout(self)
        vLayout.addWidget(self.listView)
        self.setLayout(vLayout)
        print(2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = TestWidget()
    test.show()
    app.exec()
