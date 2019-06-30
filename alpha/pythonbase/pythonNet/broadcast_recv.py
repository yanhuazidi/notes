'''收广播'''

from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.bind(("0.0.0.0",9999))

try:
    while True:
            msg,addr = s.recvfrom(1024)
            print("从{}获取广播:{}".format(addr,msg.decode()))           
except KeyboardInterrupt:
    print("\n退出广播")
except Exception as e:
    print(e)
finally:
    s.close()

