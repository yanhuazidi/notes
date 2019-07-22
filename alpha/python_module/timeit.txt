#coding=utf-8

import timeit
from timeit import Timer

def test1():
    L = []
    for i in range(1000):
        L = L +[i]

def test2():
    L = []
    for i in range(1000):
        L.append(i)

def test3():
    L = [i for i in range(1000)]

def test4():
    L = list(range(1000))

t1 = Timer("test1()","from __main__ import test1")
print("test1",t1.timeit(number=10000))
t2 = Timer("test2()","from __main__ import test2")
print("test2",t2.timeit(number=10000))
t3 = Timer("test3()","from __main__ import test3")
print("test3",t3.timeit(number=10000))
t4 = Timer("test4()","from __main__ import test4")
print("test4",t4.timeit(number=10000))

pop_zero = Timer("x.pop(0)","from __main__ import x")
pop_end = Timer("x.pop()","from __main__ import x")
print("pop(0)  pop()")
x = list(range(1000000))
pe = pop_end.timeit(number=1000)
pz = pop_zero.timeit(number=1000)
print(pe)
print(pz)