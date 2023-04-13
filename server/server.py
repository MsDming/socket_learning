import socketserver
import ast

from client.utils.models import Channel

IP = "localhost"
PORT = 5000
ADDR = (IP, PORT)
BUFF_SIZE = 1024


class MyHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # 根据requestType处理Client请求
        def parser_request(self, requestData):
            print(111)
            requestType = requestData['type']
            if requestType == 'channels':
                res = [Channel(0, '频道1').to_dict(), Channel(0, '频道2').to_dict()]
                self.request.sendall(res.__str__().encode('utf-8'))
            elif requestType == 'login':
                account, password = requestData['account'], requestData['password']
                if (account, password) == ('root', '111111'):
                    self.request.sendall({'success': True, 'nickName': '飞翔的企鹅'}.__str__().encode('utf-8'))
                else:
                    self.request.sendall({'success': False}.__str__().encode('utf-8'))

        print("conn:", self.request)
        print("addr:", self.client_address)
        while True:
            try:
                requestData = self.request.recv(BUFF_SIZE).decode('utf-8')
                requestData = ast.literal_eval(requestData)
                print(type(requestData))
                print(requestData)
                parser_request(self, requestData)

                # if data == b'': break
                # data = data.decode("utf-8")
                # print("Message:", data)
                # self.request.sendall(data.encode("utf-8"))
            except Exception as e:
                print(e)
                break


if __name__ == "__main__":
    s = socketserver.ThreadingTCPServer(ADDR, MyHandler)
    s.serve_forever()
