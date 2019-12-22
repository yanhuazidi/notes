''' 客户端　ＵＤＰ'''

from socket import *
import sys

sockfd = socket(AF_INET,SOCK_DGRAM)
if len(sys.argv)<3:
    print("输入有误")
    quit()

host = sys.argv[1]
port = int(sys.argv[2])
server_addr = (host,port)

try:
    while True:
        data = input("请输入:")
        if data == "exit":
            break
        n = sockfd.sendto(data.encode(),server_addr)
        print("发送成功",n,'beyes')
        print("等待对方消息...")
        msg,server_addr = sockfd.recvfrom(1024)
        print("服务器:",msg.decode())
except KeyboardInterrupt:
    print("\n已强制退出")
finally:
    sockfd.close()
