'''select ＩＯ多路复用


tcp套接字
'''

from select import select
from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind(("127.0.0.1",5555))
s.listen(3)

print("监控IO")
rlist = [s]
wlist = []
xlist = [s]
while True:         #以大的循环来使用select
    print("等待连接")
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print("收到:",data.decode())
            # r.send("收到消息".encode())
            wlist.append(r)

    for w in ws:
        w.send("get infometion".encode())
        wlist.remove(w)
    for x in xs:
        pass
