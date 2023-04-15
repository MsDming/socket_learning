import ast
import base64
import sys
import pymysql
from PyQt5.QtCore import QFile, QIODevice
from PyQt5.QtNetwork import QTcpServer, QHostAddress, QTcpSocket
from PyQt5.QtWidgets import QApplication
from client.utils.models import Channel


class MyServer(QTcpServer):
    def __init__(self):
        super().__init__()
        self.db = pymysql.connect(host="47.113.229.66", port=3306, user='root', password='111111', database='pysocket')
        self.channelList = []  # 频道列表，item类型为Channel
        self.allClientSkts = []  # 存储所有连接到的socket，为了保持socket不被释放
        self.load_channels_list()
        self.clientLsEachChannel = [[] for i in range(len(self.channelList) + 1)]  # 按频道存储每个来自chatWindow的socket
        self.listen(QHostAddress.LocalHost, port=5000)

    def incomingConnection(self, socketDescriptor):  # 收到新的连接请求
        try:
            clientSkt = QTcpSocket()
            clientSkt.setSocketDescriptor(socketDescriptor)
            clientSkt.readyRead.connect(self.handle_recv_msg)
            clientSkt.disconnected.connect(self.handle_client_disconnect)
            self.allClientSkts.append(clientSkt)
            print("New client connect from {}:{}".format(clientSkt.peerAddress().toString(), clientSkt.peerPort()))
        except Exception as e:
            print(e)

    def load_channels_list(self):
        with self.db.cursor() as cursor:
            sql_get_channels = """select * from channel"""
            cursor.execute(sql_get_channels)
            res = cursor.fetchall()
            self.channelList = [Channel(i[0], i[1]) for i in res]

    def handle_client_disconnect(self):
        clientSkt = self.sender()
        clientSkt.deleteLater()
        if clientSkt in self.allClientSkts:
            print("Disconnect with {}:{}".format(clientSkt.peerAddress().toString(), clientSkt.peerPort()))
            self.allClientSkts.remove(clientSkt)
        for i in self.clientLsEachChannel:
            if clientSkt in i:
                i.remove(clientSkt)

    def handle_recv_msg(self):
        def handle_login():
            with self.db.cursor() as cursor:
                sql_search_user = """select * from user where account={}""".format(account)
                print("SQL:{}".format(sql_search_user))
                resNums = cursor.execute(sql_search_user)
                # 不存在该用户
                if resNums == 0:
                    tcpSkt.write({'loginSuccess': False}.__str__().encode('utf-8'))
                    return
                queryRes = cursor.fetchone()
                assert len(queryRes) == 3
                # 密码错误
                if password != queryRes[1]:
                    tcpSkt.write({'loginSuccess': False}.__str__().encode('utf-8'))
                    return
                # 登陆成功
                nickname = queryRes[2]
                tcpSkt.write({'loginSuccess': True, 'nickname': nickname}.__str__().encode('utf-8'))
                print("用户 {} 登录".format(account))

        def handle_sendHtmlMsg():
            msgToBroadcast = {"type": "broadcastMsg", 'sendTimeStamp': sendTimeStamp, 'senderAccount': senderAccount,
                              'inputHtmlMsg': inputHtmlMsg, 'senderNickname': senderNickname}.__str__()
            print(f'msgToBroadcast:{msgToBroadcast}')
            for i in self.clientLsEachChannel[channelIndex]:
                if i != tcpSkt:
                    i.write(msgToBroadcast.encode('utf-8'))

        def handle_sendFile():
            tcpSkt.waitForReadyRead()
            fileData = tcpSkt.read(BUFF_SIZE)
            while len(fileData) < fileSize:
                tcpSkt.waitForReadyRead()
                fileData += tcpSkt.read(BUFF_SIZE)
            savedFile = QFile(f"./tempFiles/channel{channelIndex}/{fileName}")
            savedFile.open(QIODevice.WriteOnly)
            savedFile.write(fileData)
            savedFile.close()
            broadcastFile = {"type": "broadcastFile", "sendTimeStamp": sendTimeStamp, "senderAccount": senderAccount,
                             "senderNickname": senderNickname, "fileName": fileName}.__str__()
            for client in self.clientLsEachChannel[channelIndex]:
                if client != tcpSkt:
                    client.write(broadcastFile.encode('utf-8'))

        try:
            print("---------------------------------------------------------------------")
            self.db.ping(True)
            tcpSkt = self.sender()
            msg = tcpSkt.read(BUFF_SIZE).decode('utf-8')
            # print(1)
            requestDict = ast.literal_eval(msg)
            # print(2)
            assert type(requestDict) == dict
            requestType = requestDict["type"]

            if requestType == 'channels':  # 请求获取频道列表
                res = [i.to_dict() for i in self.channelList]
                tcpSkt.write(res.__str__().encode('utf-8'))

            elif requestType == 'login':  # 请求登录
                account, password = requestDict['account'], requestDict['password']
                handle_login()

            elif requestType == 'chatLogs':
                channelIndex = requestDict["channelIndex"]
                if tcpSkt not in self.clientLsEachChannel[channelIndex]:
                    self.clientLsEachChannel[channelIndex].append(tcpSkt)
                tcpSkt.write({"type": "chatLogs"}.__str__().encode('utf-8'))
                pass

            elif requestType == 'sendHtmlMsg':
                channelIndex = requestDict['channelIndex']
                senderAccount = requestDict['senderAccount']
                inputHtmlMsg = requestDict['inputHtmlMsg']
                sendTimeStamp = requestDict['sendTimeStamp']
                senderNickname = requestDict['senderNickname']
                handle_sendHtmlMsg()

            elif requestType == 'sendFile':
                channelIndex = requestDict['channelIndex']
                senderAccount = requestDict['senderAccount']
                sendTimeStamp = requestDict['sendTimeStamp']
                senderNickname = requestDict['senderNickname']
                fileSize = requestDict['fileSize']
                fileName = requestDict['fileName']
                tcpSkt.readyRead.disconnect(self.handle_recv_msg)
                print("解绑")
                handle_sendFile()
                tcpSkt.readyRead.connect(self.handle_recv_msg)

        except Exception as e:
            print(e)
        finally:
            pass


if __name__ == '__main__':
    BUFF_SIZE = 1024 * 1024 * 1024
    app = QApplication(sys.argv)
    server = MyServer()
    app.exec()
