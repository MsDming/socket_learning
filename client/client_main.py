import sys

from PyQt5.QtWidgets import QApplication

from windows.loginWindow import LoginMw

if __name__ == "__main__":
    print(sys.path)
    IP = "localhost"
    PORT = 5000
    ADDR = (IP, PORT)
    app = QApplication(sys.argv)
    loginMw = LoginMw()
    app.exec()
