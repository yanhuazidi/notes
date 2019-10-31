
from socketserver import *

class Server(ThreadingMixIn,UDPServer):
    pass

class Handler(DatagramRequestHandler):
    def handle(self):
        while True:
            data = self.rfile.readline()
            if not data:
                break
            print(data.decode())
            self.wfile.write(b'ggggggggggg')

if __name__=="__main__":
    server = Server(("0.0.0.0",8888),Handler)
    print("等待链接...")
    server.serve_forever()