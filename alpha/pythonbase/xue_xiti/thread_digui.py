
import time
import threading

def profile(fun):
    def wrapper(*args,**kwargs):
        start = time.time()
        fun(*args,**kwargs)
        end = time.time()
        print('COST:{}'.format(end-start))
    return wrapper

def fib(n):
    if n<=2:
        return 1
    return fib(n-2)+fib(n-1)

@profile
def nothread():
    fib(35)

@profile
def hasthread():
    t = threading.Thread(target=fib,args = (5,))
    t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()

nothread()
hasthread()