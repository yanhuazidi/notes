''' 服务器　ＵＤＰ　'''

from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)
server_addr = ('0.0.0.0',8888)
sockfd.bind(server_addr)

def recvfrom_sendto(sockfd):
    while True:
        print("等待对方中...")
        data,addr = sockfd.recvfrom(1024)
        print("客户端:",data.decode())
        s = input("请输入:")
        if s =='exit':
            return
        sockfd.sendto(s.encode(),addr)
try:
    recvfrom_sendto(sockfd)
except KeyboardInterrupt:
    print("\n已强制退出")
finally:
    sockfd.close()