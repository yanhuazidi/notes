import gevent
from gevent import monkey
monkey.patch_all()

from socket import *

def server():
    s = socket()
    s.bind(("0.0.0.0",8888))
    s.listen(10)
    while True:
        c,addr = s.accept()
        print("connect from:",addr)
        gevent.spawn(handle,c)
        
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"xxxxxxxxxxxx")
    c.close()

server()