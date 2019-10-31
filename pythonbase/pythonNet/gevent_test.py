import gevent

def foo():
    print("Running foo")
    gevent.sleep(2)
    print("Running foo again")

def bar():
    print("Running bar")
    gevent.sleep(3)
    print("Running bar again")

f = gevent.spawn(foo)
g = gevent.spawn(bar)

gevent.joinall([f,g])

