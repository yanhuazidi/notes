
'''
HTTP Server v2.0
可以做request解析
能够返回简单的数据
使用类进行封装
'''
from socket import *
from threading import Thread
import sys

class HTTPServer:
    def __init__(self,server_addr,stati_dir):
        self.server_addr = server_addr
        self.stati_dir = stati_dir
        self.port = self.server_addr[1]
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_addr)

    def server_forever(self):
        self.sockfd.listen(5)
        print("listen the port %d"%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("Error:",e)
                continue
            clienthread = Thread(target=self.handle,args=(connfd,))
            clienthread.setDaemon(True)
            clienthread.start()

    def handle(self,connfd):
        request = connfd.recv(4096)
        requestHeaders = request.splitlines()
        for lien in requestHeaders:
            print(lien.decode())
        getrequest = str(requestHeaders[0]).split(' ')[1]
        print("访问内容:",getrequest)
        if getrequest=='/' or getrequest[-5:]=='.html':
            self.get_html(connfd,getrequest)
        else:
            self.get_data(connfd,getrequest)
        connfd.close()

    def get_html(self,connfd,getrequest):
        if getrequest =='/':
            filename = self.stati_dir+'/index.html'
        else:
            filename = self.stati_dir+getrequest
        print(filename)
        try:
            f = open(filename)
        except Exception:
            responseHeaders="HTTP/1.1 404 Not found\r\n"
            responseHeaders+='\r\n'
            responseBoby="Sorry,not found the page!"
        else:
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders+= '\r\n'
            responseBoby = f.read()
        finally:
            reponse = responseHeaders + responseBoby
            connfd.send(reponse.encode(encoding='gbk'))

    def get_data(self,connfd,getrequest):
        urls = ['/time','/tedu','/python']
        if getrequest in urls:
            responseHeaders = 'HTTP/1.1 200 OK\r\n'
            responseHeaders+='\r\n'
            if getrequest =='/time':
                import time
                responseBoby = time.ctime()
            elif getrequest=='/tedu':
                responseBoby ='Tedu python'
            elif getrequest=='/python':
                responseBoby = '欲与天公试比高'
        else:
            responseHeaders = "HTTP/1.1 404 Not found\r\n"
            responseHeaders+='\r\n'
            responseBoby ="何当共剪西窗烛,却话巴山夜雨时"
        response = responseHeaders + responseBoby
        connfd.send(response.encode(encoding='gbk'))
if __name__ == '__main__':
    server_addr = ('0.0.0.0',8800)
    stati_dir = '/home/tarena/test/pythonNet/zi_liao'
    httpd = HTTPServer(server_addr,stati_dir)
    httpd.server_forever()