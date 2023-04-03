import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from client.ui_py.ui_hall import Ui_hall
from client.utils.model import Channel


class HallFrm(QMainWindow, Ui_hall):
    def __init__(self):
        super().__init__()
        self.user = None
        self.setupUi(self)
        self.listWidget_channels

    def connect_signals_slots(self):
        pass

    def get_user_from_parent(self, user):
        self.user = user
        self.setWindowTitle(self.user.nickName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    hallFrm = HallFrm()
    hallFrm.show()
    app.exec()
