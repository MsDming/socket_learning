import base64
import re
import sys
import urllib.request

import urllib3.request
from PyQt5.QtWidgets import QWidget, QFileDialog, QApplication

from client.ui_py.ui_chat import Ui_chatWindow
from client.utils.models import Channel

class ChatWindow(QWidget, Ui_chatWindow):
    def __init__(self, channel: Channel = None):
        super().__init__()
        self.user = None
        self.setupUi(self)
        self.pushButton_send.clicked.connect(self.send_message)
        self.pushButton_sendImg.clicked.connect(self.send_img)

    def send_message(self):
        html = self.textEdit_input.toHtml()
        print(html)
        image_data_list = []
        for match in re.finditer(r'<img[^>]*src="([^"]+)"[^>]*>', html):
            image_file_path = match.group(1)
            print(f"Image path:{image_file_path}")
            img_format = image_file_path.split('.')[-1]
            with urllib.request.urlopen(url=image_file_path) as f:
                image_data = f.read()
                image_data_base64 = base64.b64encode(image_data).decode('utf-8')
                image_data_list.append(image_data_base64)
            html = html.replace(image_file_path, 'data:image/{1};base64,{0}'.format(image_data_base64, img_format))
        self.textBrowser_show.textCursor().insertHtml(html)
        self.textBrowser_show.textCursor().insertHtml('<br>')
        self.textEdit_input.clear()

    def send_img(self):
        file_path, _ = QFileDialog.getOpenFileName(self, '选择图片', '', 'Images (*.png *.xpm *.jpg *.gif)')
        if file_path:
            with open(file_path, 'rb') as f:
                image_data = f.read()
                image_base64 = base64.b64encode(image_data).decode('utf-8')
                self.textBrowser_show.textCursor().insertHtml(f'<img src="data:image/png;base64,{image_base64}">')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat = ChatWindow()
    chat.show()
    app.exec()
