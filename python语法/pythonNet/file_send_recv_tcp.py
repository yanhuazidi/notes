'''文件收发　TCP'''


from socket import *
import os

def file_send(sockfd): 
    while True:
        print("输入exit退出")
        data = input("请输入文件路径:")
        if data == 'exit':
            return
        if os.path.exists(data.strip()):
            files = os.path.split(data)[1]
            sockfd.send(files.encode())
            _ok = sockfd.recv(1024)
            if _ok.decode()=='ok':
                with open(data,'rb') as f:
                    while True:
                        x = f.read(1024000)
                        if not x:
                            break
                        sockfd.send(x)
                print("传输完成")
                return
            else:
                print("接收失败")
        else:
            print("路径不正确！！！")

def file_recv(connfd):
    print("客户端输入...")
    path = connfd.recv(1024)
    _file = path.decode()
    _path = os.path.join(os.getcwd(),_file)
    if _path != '':
        with open(_path,'wb') as f:
            connfd.send('ok'.encode())
            while True:
                data = connfd.recv(2048000)
                if not data:
                    break
                f.write(data)
        print("传输完成")
        return
    print("传输失败")
