from tornado.web import Application,RequestHandler
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import define,parse_config_file,options



class IndexHandler(RequestHandler):
    def get(self):
        self.write('<a href=/java>Hello World go java</a>')
        self.write('<br><a href=/python>Hello World go python</a>')
    def post(self):
        pass
class JavaHandler(RequestHandler):
    def get(self,day=None,input=None):

        self.write('Hello Java')
        if day:
            self.write('Hello '+day)
        if input:
            self.write('Hello '+input)
    def post(self):
        pass

class PythonHandler(RequestHandler):
    #覆盖RequestHandler  get方法，响应get请求
    def get(self):
        self.write('Hello Python')
        #GET获取参数 http://127.0.0.1:9999/python?day=111111111
        day = self.get_query_argument('day',default='0000000',strip=False)
        print(self.request)
        self.write('Hello Python'+day)
        #/python?day=1&day=2&day=3&day=4&day=5
        day = self.get_query_arguments('day',strip=False)
        print(day)#[1,2,3,4,5]
    #覆盖RequestHandler  post方法，响应post请求
    def post(self):
        day = self.get_body_argument('day',default='0000000',strip=False)
        self.write('Hello Python'+day)
        day = self.get_body_arguments('day',strip=False)
        print(day)

define('port',type=int,default=8888)

parse_config_file('config/config.txt')



app = Application(handlers=[('/',IndexHandler),
                            ('/java',JavaHandler),
                            ('/java/([0-9]*)/([a-z0-9]*)',JavaHandler),
                            ('/python',PythonHandler)])

server = HTTPServer(app)
server.listen(options.port)

IOLoop.current().start()
