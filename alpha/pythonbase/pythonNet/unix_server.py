'''本地套接字　　服务器'''

from socket import *

sock_file = './sock'

sockfd = socket(AF_UNIX,SOCK_STREAM)

sockfd.bind(sock_file)

sockfd.listen(5)

while True:
    print("等待连接...")
    c,addr = sockfd.accept()
    while True:
        print("等待输入..."")
        data = c.recv(1024)
        if not data:
            break
        print('客户端:',data.decode())
    c.close()
sockfd.close()