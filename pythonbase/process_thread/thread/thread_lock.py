

from threading import Lock,Thread

a = b =0

l = Lock()
def value():
    while True:
        l.acquire()
        if a != b:
            print("a = %d,b = %d"%(a,b))
        l.release()

t = Thread(target=value)

t.start()
while a <100:
    with l:
        a +=1
        b +=2
t.join()