from threading import Event,Thread
from time import sleep

s = None
e = Event()

def bar():
    print("Bar 拜山头")
    global s
    sleep(1.5)
    s = "大地"
    e.set()
    e.wait()

b = Thread(target=bar)
b.start()

sleep(1)

print("口令")
for _ in [1,2]:
    e.wait()
    if s =='大地':
        print("啊！大海")
    else:
        print("好多水")
    e.clear()

b.join()