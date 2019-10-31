from socket import *
from time import sleep,ctime

sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
sockfd.bind(('127.0.0.1',8888))
sockfd.listen(3)
# sockfd.setblocking(False)
sockfd.settimeout(5)

while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd._accept()
    # except BlockingIOError:
    #     sleep(2)
    #     print(ctime()[11:19])
    #     continue
    except timeout:
        print("时间:",ctime()[11:19])
        continue
    else:
        print("Connect from",addr)
        data = connfd.recv(1024)
        print("Receive",data)
        connfd.close()