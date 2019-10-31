'''TCP  客户端

'''
from socket import *
import sys

def sys_argv():
    '''命令行传参,返回服务器地址元组'''
    if len(sys.argv)<3:
        print("输入有误")
        quit()
    host = sys.argv[1]
    port = int(sys.argv[2])
    server_addr = (host,port)
    return server_addr
    
def recv_send(sockfd):
    '''输出输入'''
    print("输入 exit 断开连接")
    while True:
        data = input("请输入:")
        if data == 'exit':
            return
        sockfd.send(data.encode())
        print("等待服务器...")
        data = sockfd.recv(1024)
        if not data:
            print("服务器断开")
            return
        print("服务器:",data.decode())
    
def connect_host(server_addr,functino_send_recv):
    '''创建套接字连接服务器,传入服务器地址元组和传输函数'''
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    try:
        sockfd.connect(server_addr)
    except ConnectionRefusedError:
        print("连接失败,请求被拒绝!!!")
        return
    try:
        functino_send_recv(sockfd)
    except KeyboardInterrupt:
        print("\n已强制退出")
    finally:
        sockfd.close()

if __name__ == "__main__":
    server_addr = sys_argv()
    # server_ip = input("服务器地址:")
    # server_port = int(input('端口号:'))
    # server_addr = (server_ip,server_port)
    connect_host(server_addr,recv_send)