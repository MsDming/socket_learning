import sys

from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication, QMainWindow, QHBoxLayout, \
    QVBoxLayout, QLineEdit, QTextBrowser


class ClientFrm(QMainWindow):
    def __init__(self, ADDR=("localhost", 5000)):
        super().__init__()
        self.tcpSocket = QTcpSocket(parent=self)
        self.tcpSocket.connectToHost(ADDR[0], ADDR[1])
        self.tcpSocket.readyRead.connect(self.recv_message)
        self.init_view()

    def init_view(self):
        layout = QVBoxLayout()
        self.resize(500, 500)
        self.textField = QTextBrowser()
        layout.addWidget(self.textField)
        self.lineEdit = QLineEdit()
        layout.addWidget(self.lineEdit)
        self.btnSend = QPushButton("发  送")
        self.btnSend.clicked.connect(self.send_message)
        self.btnClear = QPushButton("清  空")
        self.btnClear.clicked.connect(self.clear_text)
        layout2 = QHBoxLayout()
        layout2.addWidget(self.btnSend)
        layout2.addWidget(self.btnClear)
        layout.addLayout(layout2)
        self.setWindowTitle("hello,pyqt5!")
        self.widget = QWidget()
        self.widget.setLayout(layout)
        self.setCentralWidget(self.widget)

    def send_message(self):
        text = self.lineEdit.text()
        print(text[-1])
        self.tcpSocket.write(text.encode("utf-8"))
        self.clear_text()
        self.textField.append(text)

    def recv_message(self):
        data = self.tcpSocket.read(1024)
        data = data.decode('utf-8')
        print("type(data):{}".format(type(data)))
        self.textField.append(data)

    def clear_text(self):
        self.lineEdit.clear()


if __name__ == "__main__":
    IP = "localhost"
    PORT = 5000
    ADDR = (IP, PORT)
    app = QApplication(sys.argv)
    clientFrm = ClientFrm(ADDR)
    clientFrm.show()
    app.exec()
