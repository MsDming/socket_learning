from PyQt5.QtWidgets import QWidget

from client.ui_py.ui_chat import Ui_chatWindow


class ChatWindow(QWidget,Ui_chatWindow):
    def __init__(self):
        super().__init__()
        self.setupUi()
