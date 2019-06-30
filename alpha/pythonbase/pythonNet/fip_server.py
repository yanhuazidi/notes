
from socket import *
from threading import Thread
import os,sys
import time

HOST = '0.0.0.0'
PORT = 7777
ADDR = (HOST,PORT)
FILE_PATH ='/home/tarena/test/pythonNet/zi_liao/'

class FtpServer:
    def __init__(self,connfd):
        self.connfd = connfd
    
    def do_list(self):
        print("执行list")
        file_list = os.listdir(FILE_PATH)
        if not file_list:
            self.connfd.send("文件库为空".encode())
            return
        else:
            files = ''
            for _file  in file_list:
                if _file[0] !='.' and os.path.isfile(FILE_PATH+_file):
                    files += '#'+_file
            self.connfd.send(files.encode())
    
    def do_get(self,filename):
        try:
            with open(FILE_PATH+filename,'rb') as f:
                self.connfd.send('OK'.encode())
                time.sleep(0.1)
                while True:
                    data = f.read(1024)
                    if not data:
                        self.connfd.send(b'#')
                        print("发送完成")
                        return
                    self.connfd.send(data)           
        except:
            self.connfd.send("文件不存在".encode())
            return

    def do_put(self,filename):
        if filename in os.listdir(FILE_PATH):
            self.connfd.send("文件已存在".encode())
            return
        try:
            with open(FILE_PATH+filename,'wb') as f:
                self.connfd.send('OK'.encode())
                while True:
                    data = self.connfd.recv(1024)
                    if data=='#'.encode():
                        print("接收完成")
                        return           
                    f.write(data)
        except:
            self.connfd.send("文件创建失败".encode())
            print("文件创建失败")
            return
def guan():
    os.wait()
    sys.exit()

def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(ADDR)
    sockfd.listen(5)
    t_L = []
    while True:
        print("等待连接中...")
        try:
            connfd,addr = sockfd.accept()
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("服务器退出")
        except Exception as e:
            print("Error:",e)
            continue
        print("连接用户端:",addr)
        pid = os.fork()
        if pid ==0:
            ftp = FtpServer(connfd)
            sockfd.close()
            while True:
                data = connfd.recv(1024).decode()
                if not data or data =='exit':
                    sys.exit("客户端退出")
                elif data[0]=='L':
                    ftp.do_list()
                elif data[0]=='G':
                    filename = data[2:]
                    ftp.do_get(filename)
                elif data[0]=='P':
                    filename = data[2:]
                    ftp.do_put(filename)
        elif pid >0:
            print(os.getpid())
            connfd.close()
            t = Thread(target=guan)
            t.start()
            t_L.append(t)
            for i in t_L[:]:
                if not i.is_alive():
                    i.join()
                    t_L.remove(i)                    
            continue
        else:
            print("连接失败")
            continue
if __name__=="__main__":
    main()
