#coding=utf-8
'''
HTTP Server v2.0
多线程并发
可以做request解析
能够返回简单的数据
使用类进行封装
'''

from socket import *
from threading import Thread 
import sys 

#封装具体的http server功能
class HTTPServer(object):
    def __init__(self,server_addr,static_dir):
        #添加对象属性
        self.server_address = server_addr
        self.static_dir = static_dir
        self.ip = server_addr[0]
        self.port = server_addr[1]
        #创建套接字
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,\
        SO_REUSEADDR,1) 
        self.sockfd.bind(self.server_address)
    
    #启动服务器
    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen the port %d"%self.port)
        while True:
            try:
                connfd,addr = self.sockfd.accept()
            except KeyboardInterrupt:
                self.sockfd.close()
                sys.exit("服务器退出")
            except Exception as e:
                print("Error:",e)
                continue 
            #创建线程处理客户端请求
            clientThread = Thread(\
            target=self.handle,args=(connfd,))
            clientThread.setDaemon(True)
            clientThread.start()
    
    #具体处理客户端请求
    def handle(self,connfd):
        #接收客户端请求
        request = connfd.recv(4096)
        #按行切割
        requestHeaders = request.splitlines()
        print(connfd.getpeername(),":",\
        requestHeaders[0])

        #获取具体请求内容
        getRequest=str(requestHeaders[0]).split(' ')[1]  
        
        if getRequest=='/' or getRequest[-5:]=='.html':
            self.get_html(connfd,getRequest)
        
        connfd.close()

    #给客户端发送网页
    def get_html(self,connfd,getRequest):
        if getRequest == '/':
            filename = self.static_dir+"/index.html"
        else:
            filename = self.static_dir+getRequest
        # print(filename)
        try:
            f = open(filename)
        except Exception:
            #没找到网页
            responseHeaders="HTTP/1.1 404 Not found\r\n"
            responseHeaders += '\r\n'
            responseBody = "Sorry,not found the page"
        else:
            #如果找到网页则返回网页
            responseHeaders="HTTP/1.1 200 OK\r\n"
            responseHeaders += '\r\n'
            responseBody = f.read()
        finally:
            response=responseHeaders+responseBody
            connfd.send(response.encode())

if __name__ == "__main__":
    #用户使用时自己设定服务器ＩＰ
    server_addr = ('0.0.0.0',8000)
    #需要用户提供网页位置
    static_dir = "./zi_liao"

    #创建服务器对象
    httpd = HTTPServer(server_addr,static_dir) 
    #启动服务器
    httpd.serve_forever()
