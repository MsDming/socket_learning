import ast
import sys

from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox

from client.ui_py.ui_register import Ui_Register


class RegisterMw(Ui_Register, QWidget):
    def __init__(self, IP: str):
        super().__init__()
        self.setupUi(self)
        self.label_prompt.setStyleSheet("""QLabel{color:red;}""")
        self.IP = IP
        self.pushButton_flushInput.clicked.connect(self.flush_input)
        self.pushButton_submit.clicked.connect(self.submit_register)
        self.tcpSkt = QTcpSocket(self)
        self.tcpSkt.connectToHost(self.IP, 5000)
        self.tcpSkt.readyRead.connect(self.handle_register_response)

    def submit_register(self):
        nickName = self.lineEdit_nickname.text()
        password1 = self.lineEdit_password1.text()
        password2 = self.lineEdit_password2.text()
        if password1 != password2:
            self.label_prompt.setText("两次密码输入不一致，请重试")
            return
        if len(password1) > 20:
            self.label_prompt.setText("密码长度不应超过20，请重试")
            return
        self.label_prompt.clear()
        self.tcpSkt.write({"type": "register", "nickName": nickName, "password": password2}.__str__().encode('utf-8'))

    def flush_input(self):
        self.lineEdit_password1.clear()
        self.lineEdit_password2.clear()
        self.lineEdit_nickname.clear()

    def handle_register_response(self):
        responseDict = ast.literal_eval(self.tcpSkt.read(1024).decode('utf-8'))
        if responseDict['registerSuccess']:
            account = responseDict["account"]
            QMessageBox.information(self, "提示", f'注册成功\n账号：{account}')
            self.close()
            self.deleteLater()
            return
        else:
            self.label_prompt.setText("注册失败，请重试")
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = RegisterMw("127.0.0.1")
    mw.show()
    app.exec()
