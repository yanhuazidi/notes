''' http 服务器


响应浏览器
'''

from socket import *


def handleClient(connfd):
    request = connfd.recv(4096)
    request_lines = request.splitlines()    #切割字节串方法
    for line in request_lines:
        print(line)
    try:
        f = open('index.html')
    except IOError:
        response = "HTTP/1.1 404 Not Found\r\n"
        response +='\r\n'
        response +="======Sorry not found======"
    else:
        response = "HTTP/1.1 200 OK Found\r\n"
        response +='\r\n'
        response +=f.read()
    finally:
        connfd.send(response.encode())
        f.close()      

def main():
    sockfd = socket()
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    sockfd.bind(("0.0.0.0",8800))
    sockfd.listen(5)
    print("Listen to the port 8800")
    while True:
        connfd,addr = sockfd.accept()
        handleClient(connfd)
        connfd.close()

if __name__ == "__main__":
    main()