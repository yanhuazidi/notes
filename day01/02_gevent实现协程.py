import gevent
import time
from gevent import monkey
# 修改阻塞行为
monkey.patch_time()

def f1():
    print("开始执行函数 1")
    time.sleep(2)
    print('函数1执行结束')

def f2():
    print("开始执行函数 2")
    time.sleep(3)
    print('函数2执行结束')

# 创建协程对象
g1 = gevent.spawn(f1)
g2 = gevent.spawn(f2)
# 启动协程
gevent.joinall([g1,g2])



