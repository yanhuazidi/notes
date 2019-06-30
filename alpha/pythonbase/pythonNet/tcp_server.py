'''服务器端	TCP'''

import socket


def recv_send(connfd):
    '''　服务器收发功能  '''
    while True:
        print("等待客户输入...")
        data = connfd.recv(2048)
        if not data:
            print("客户端断开")
            return
        print("客户端：",data.decode())
        s = input("请输入:")
        if s == 'exit':
            return
        else:
            connfd.send(s.encode())
            
def _fuwuqi(recv_send):
    ''' 创建tcp套接字，客户端连接 '''
    server_ip = input("主机地址:")
    server_port = int(input('端口号:'))
    server_addr = (server_ip,server_port)
    sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockfd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sockfd.bind(server_addr)
    sockfd.listen(5)
    while True:
        try:
            print("等待客户连接．．．")
            connfd,addr = sockfd.accept()
            print("已连接,客户地址:",addr)
            recv_send(connfd)
            connfd.close()
        except KeyboardInterrupt:
            print("\n已强制退出")
        finally:
            sockfd.close()
            return

if __name__=="__main__":
    _fuwuqi(recv_send)

