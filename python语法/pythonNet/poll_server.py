'''poll 　ＩＯ多路复用

服务器
'''
from socket import *
from select import *

s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('0.0.0.0',8888))
s.listen(3)

p = poll()

fdmap = {s.fileno():s}
p.register(s,POLLIN|POLLERR)

while True:
    print("等待IO...")
    events = p.poll()
    print(events)
    for fd,event in events:
        if fd ==s.fileno():
            c,addr =fdmap[fd].accept()
            print("Connect from",addr)
            p.register(c,POLLIN | POLLERR)
            print(POLLIN)
            fdmap[c.fileno()] = c
        elif event & POLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
            else:
                print("Receive:",data.decode())
                fdmap[fd].send("收到啦".encode())