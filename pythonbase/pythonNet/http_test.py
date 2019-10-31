
from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",8000))

s.listen(3)

while True:
    c,addr = s.accept()
    print("Connect from",addr)
    data = c.recv(4096)
    print("*************")
    print(data)
    print("*************")

    data = '''HTTP/1.1 200 OK
    Content-Encoding: gzip
    Content-Type:text/html

    <h1>Welcome to tedu Python</h1>
    <p>This is test</p>
    <p>wei tian hua</p>
    <p>  ^-^   </p>
    '''
    c.send(data.encode())
    c.close()

s.close()