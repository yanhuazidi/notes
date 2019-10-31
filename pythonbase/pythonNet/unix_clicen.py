'''本地套接字　客户端'''

from socket import *

sock_file = './sock'

sockfd = socket(AF_UNIX,SOCK_STREAM)

sockfd.connect(sock_file)

while True:
    data = input("请输入:")
    if not data:
        break
    sockfd.send(data.encode())
    # data = sockfd.recv(1024)