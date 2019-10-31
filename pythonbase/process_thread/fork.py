'''多进程'''

import os
from time import sleep

print("=============")
a = 1

pid = os.fork()    #原样拷贝父进程空间，新进程以赋值pid=0开始执行

if pid < 0 :
    print("Create ptocess failed")
elif pid == 0:
    print("Child PID:",os.getpid())
    print("The new process")
    print("a = %d"%a)
    a = 10000
else:
    print("Parent PID:",os.getpid())
    print("The old process")
