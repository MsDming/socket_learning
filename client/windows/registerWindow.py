from PyQt5.QtWidgets import QWidget

from client.ui_py.ui_register import Ui_Register


class RegisterMw(Ui_Register, QWidget):
    def __init__(self, IP: str):
        super().__init__()
        self.setupUi(self)
        self.IP = IP
