from select import *
from time import sleep
import sys

print(sys.stdin.fileno())
print(sys.stdout.fileno())
print(sys.stderr.fileno())

rlist = [sys.stdout]
wlist = [sys.stdin]
xlist = []

while True:
    print("select　阻塞．．．")
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        if r ==sys.stdin:
            sys.stdin.write()
    for w in ws:
        if w ==sys.stdout:
            sys.stdout.read()