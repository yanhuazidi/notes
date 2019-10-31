import gevent
from gevent import monkey
monkey.patch_socket()
import socket

# 创建TCP套接字
def Server():
    server = socket.socket(
                socket.AF_INET,
                socket.SOCK_STREAM)
    # 设置端口复用
    server.setsockopt(socket.SOL_SOCKET,
                    socket.SO_REUSEADDR,
                    1)
    server.bind(('127.0.0.1',8888))
    server.listen(10)
    print('正在等待客户端连接......')
    while True:
        client,addr = server.accept()
        print(addr,'连接过来了')
        # 协程，接收多个客户端连接，实现并发
        gevent.spawn(f1,client)


# 处理客户端函数
def f1(client):
    while True:
        data = client.recv(1024)
        if not data:
            break 
        client.send('服务端收到'.encode())

if __name__ == '__main__':
    Server()









