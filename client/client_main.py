import sys

import qdarkstyle
from PyQt5.QtWidgets import QApplication
from qdarkstyle import LightPalette

from windows.loginWindow import LoginMw

if __name__ == "__main__":
    print(sys.path)
    IP = "localhost"
    PORT = 5000
    ADDR = (IP, PORT)
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
    loginMw = LoginMw()
    app.exec()
