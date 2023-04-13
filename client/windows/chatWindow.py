import ast
import base64
import re
import time
import urllib.request
import sys


sys.path.append(r'D:\Study\计算机网络\socket_learning')
from PyQt5.QtNetwork import QTcpSocket
from PyQt5.QtWidgets import QWidget

from client.ui_py.ui_chat import Ui_chatWindow
from client.utils.models import Channel


class ChatWindow(QWidget, Ui_chatWindow):
    def __init__(self, channel: Channel):
        super().__init__()
        self.user = None
        self.setupUi(self)
        self.channel = channel
        self.setWindowTitle(self.channel.channelName)
        self.label_channelName.setText(channel.channelName)
        self.tcpSkt = QTcpSocket(self)
        self.tcpSkt.connectToHost('localhost', 5000)
        self.load_chat_logs()  # 加载聊天记录
        self.pushButton_send.clicked.connect(self.send_message)

    def get_user_from_parent(self, user):
        self.user = user
        print("I have got the user info from my parent.")

    def load_chat_logs(self):  # 加载聊天记录
        self.tcpSkt.write({"type": "chatLogs", "channelIndex": self.channel.channelIndex}.__str__().encode('utf-8'))
        self.tcpSkt.readyRead.connect(self.recv_msg)
        # TODO:init chat logs
        pass

    def send_message(self):
        # 获取时间戳
        sendTimeStamp = time.time()
        self.textBrowser_show.append(
            "[{} {}]\n".format(self.user.nickname, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(sendTimeStamp))))
        # 内容转html
        htmlMsg = self.textEdit_input.toHtml()

        # html内图片转base64
        image_data_list = []
        for match in re.finditer(r'<img[^>]*src="([^"]+)"[^>]*>', htmlMsg):
            image_file_path = match.group(1)
            print(f"Image path:{image_file_path}")
            img_format = image_file_path.split('.')[-1]
            with urllib.request.urlopen(url=image_file_path) as f:
                image_data = f.read()
                image_data_base64 = base64.b64encode(image_data).decode('utf-8')
                image_data_list.append(image_data_base64)
            htmlMsg = htmlMsg.replace(image_file_path,
                                      'data:image/{1};base64,{0}'.format(image_data_base64, img_format))
        # 向服务器发送数据
        try:
            requestData = {"type": "sendHtmlMsg", "channelIndex": self.channel.channelIndex,
                           "senderAccount": self.user.account, 'inputHtmlMsg': htmlMsg,
                           'sendTimeStamp': sendTimeStamp, 'senderNickname': self.user.nickname}.__str__()
            self.tcpSkt.write(requestData.encode('utf-8'))
            self.textBrowser_show.textCursor().insertHtml(htmlMsg)
            self.textBrowser_show.textCursor().insertHtml('<br>')
            self.textEdit_input.clear()
        except Exception as e:
            print(e)

    def recv_msg(self):
        try:
            tcpSkt = self.sender()
            data = tcpSkt.read(1024).decode('utf-8')
            recvDict = ast.literal_eval(data)
            resType = recvDict["type"]
            if resType == "chatLogs":
                pass
            elif resType == "broadcastMsg":
                sendTimeStamp = recvDict["sendTimeStamp"]
                senderNickname = recvDict['senderNickname']
                htmlMsg = recvDict['inputHtmlMsg']
                self.textBrowser_show.append(
                    "[{} {}]\n".format(senderNickname,
                                       time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(sendTimeStamp))))
                self.textBrowser_show.insertHtml(htmlMsg)
                self.textBrowser_show.insertHtml("<br>")
        except Exception as e:
            print(e)
