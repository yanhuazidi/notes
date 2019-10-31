
#基于fork完成多进程网络并发

from socket import *
import os,sys
from threading import Thread

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST,PORT)
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(ADDR)
sockfd.listen(5)


def client_handler(cour):
    print(os.getpid())
    print("客户端:",cour.getpeername())
    while True:
        data = cour.recv(1024)
        if not data:
            break
        print(data.decode())
        cour.send(b'Receive your message')
    cour.close()
    sys.exit(0)

def guan():
    os.wait()
    sys.exit()

t_L = []
while True:
    print("等待连接...")
    try:
        connfd,addr = sockfd.accept()
    except KeyboardInterrupt:
        sockfd.close()
        sys.exit('退出服务器')
    except Exception as e:
        print("Error:",e)
        continue
    else:
    #  二级子进程回收子进程
        # pid = os.fork()
        # if pid ==0:
        #     p = os.fork()
        #     if p ==0:
        #         sockfd.close()
        #         client_handler(cour)
        #     else: 
        #         sys.exit(0)
        # elif pid >0:
        #     print(os.getpid())
        #     cour.close()
        #     os.wait()
        #     continue
        # else:
        #     print("连接失败")
        #     continue
    #　线程回收子进程
        pid = os.fork()
        if pid ==0:
            sockfd.close()
            client_handler(connfd)
        elif pid >0:
            print(os.getpid())
            connfd.close()
            t = Thread(target=guan)
            t.start()
            t_L.append(t)
            for i in t_L[:]:
                if not i.is_alive():
                    i.join()
                    t_L.remove(i)                    
            continue
        else:
            print("连接失败")
            continue

