

from socket import *
import sys,os
import time

class FtpClient:
    def __init__(self,sockfd):
        self.sockfd = sockfd
    
    def do_list(self):
        self.sockfd.send("L".encode())
        sbytes =self.sockfd.recv(2048).decode()
        if sbytes[0]=="#":
            sbytes = sbytes[1:].split('#')
            for x in enumerate(sbytes,1):
                print(x)
        else:
            print(sbytes)
            
    def do_fet(self,filename):
        self.sockfd.send(('G '+filename).encode())
        data = self.sockfd.recv(1024).decode()
        if data =='OK':
            with open(filename,'wb') as f:
                while True:
                    data = self.sockfd.recv(1024)
                    if data =="#".encode():
                        print("接收完成")
                        return
                    f.write(data)
    
    def do_put(self,filename):
        if not os.path.exists(filename):
            print("文件不存在")
            return
        filen = os.path.basename(filename)
        self.sockfd.send(('P '+filen).encode())
        data = self.sockfd.recv(1024).decode()
        if data=='OK':
            try:
                with open(filename,'rb') as f:
                    while True:
                        data = f.read(1024)
                        if not data:
                            time.sleep(0.1)
                            self.sockfd.send(b'#')
                            print("发送完成")
                            return
                        self.sockfd.send(data)           
            except:
                self.sockfd.send("文件打开失败".encode())
                return

def main():
    if len(sys.argv)<3:
        print("argv is error")
        return
    HOST = sys.argv[1]
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print("connectError: ",e)

    ftp = FtpClient(sockfd)
    while True:
        print("=======命令选项========")
        print(" |----   list    ----|")
        print(" |----  get file ----|")
        print(" |----  put file ----|")
        print(" |----    quit   ----|")
        print(" =====================")
        try:
            cmd = input("\n输入命令>>")
        except KeyboardInterrupt:
            sockfd.close()
            sys.exit("退出")
        except Exception as e:
            print("Error:",e)
            continue
        if cmd.strip() =='list':
            ftp.do_list()
        elif cmd.strip() =='get file':
            filename = input("请输入文件名:").strip()
            ftp.do_fet(filename)
        elif cmd.strip() =='put file':
            filename = input("请输入文件名:").strip()
            ftp.do_put(filename)
        elif cmd =='quit':
            sys.exit("退出客户端")

if __name__=="__main__":
    main()