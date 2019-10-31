from multiprocessing import Process 
from socket import *
import sys
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

def handler():
    print("Connect from:", c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send("Received".encode())
    c.close()
    sys.exit(0)    #子进程退出，不然执行下面的accept

L = []

while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        s.close()
        sys.exit("\nEXIT")
    except Exception as e:
        print(e)
        continue
    
    p = Process(target = handler)

    # p.setDaemon = True
    # p.start()
   
    p.start()
    L.append(p)
    for i in L[:]:
        if i.is_alive() == False:
            i.join()
            L.remove(i)
    