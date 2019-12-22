

from wsgiref.simple_server import make_server
# 导入我们自己编写的application函数:


def application(environ, start_response):
    for key in environ:
        print(key,':',environ.get(key))
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']

# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("服务器退出")


