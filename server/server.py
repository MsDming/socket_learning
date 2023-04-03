import socketserver

IP = "localhost"
PORT = 5000
ADDR = (IP, PORT)


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("conn:", self.request)
        print("addr:", self.client_address)
        while True:
            try:
                data = self.request.recv(1024)
                print(data)
                if data == b'': break
                data = data.decode("utf-8")
                print("Message:", data)
                self.request.sendall(data.encode("utf-8"))
            except Exception as e:
                print(e)
                break


if __name__ == "__main__":
    s = socketserver.ThreadingTCPServer(ADDR, MyServer)
    s.serve_forever()
