from threading import Thread,Lock 
import time 

# 创建两个锁对象
lock1 = Lock()
lock2 = Lock()

# 线程函数1
def f1():
    # lock1加锁
    lock1.acquire()
    print('线程1锁住了lock1')
    time.sleep(0.1)
    # 给lock2加锁
    # 此处产生了死锁，加锁时发现f2已经对lock2
    # 进行了加锁处理，阻塞
    while True:
        result = lock2.acquire(timeout=1)
        if result:
            print('线程1锁住了lock2')
            print('线程1 你好')

            # 释放锁
            lock2.release()
            break 
            # lock1.release()
        else:
            # 对lock1释放锁
            lock1.release()

# 线程函数2
def f2():
    lock2.acquire()
    print('线程2锁住了lock2')
    time.sleep(0.1)
    lock1.acquire()
    print('线程2锁住了lock1')
    print('线程2 你好')

    # 释放锁
    lock1.release()
    lock2.release()

t1 = Thread(target=f1)
t2 = Thread(target=f2)
t1.start()
t2.start()
t1.join()
t2.join()











