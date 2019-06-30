from threading import Thread,Lock

number = 2000
lock = Lock()

def f1():
    global number
    for i in range(3000000):
        lock.acquire()
        number += 1
        lock.release()
    print('线程1结束')

def f2():
    global number
    for i in range(3000000):
        lock.acquire()
        number -= 1
        lock.release()
    print('线程2结束')

t1 = Thread(target=f1)
t2 = Thread(target=f2)
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
# t1.join()
# t2.join()
print(number)

# number = number + 1
# 1. x = number + 1
# 2. number = x

# 第一次：
#   x1 = number + 1 # number:2000,x1:2001
#   x2 = number - 1 # number:2000,x2:1999
#   number = x1     # number:2001
#   number = x2     # number:1999


