
from socketserver import *

class Server(ForkingMixIn,TCPServer):
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        print("Connect from:",self.client_address)
        while True:
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'hehehehheheh')

if __name__=="__main__":
    server_addr = ("0.0.0.0",6666)

    server = Server(server_addr,Handler)
    print("等待链接...")
    server.serve_forever()