'''发广播'''

from socket import *
from time import sleep

dest = ("176.17.8.255",9999)

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

try:
    while True:
        #sleep(2)
        sss = input(">>")
        s.sendto(sss.encode(),dest)
except KeyboardInterrupt:
    print("\n强制退出")
except Exception as e:
    print(e)
finally:
    s.close()