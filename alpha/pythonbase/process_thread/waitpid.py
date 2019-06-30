
import os
from time import sleep

pid = os.fork()

if pid < 0:
    print('Create process failed')
elif pid == 0:
    sleep(3)
    print("Child %d process exit"%os.getpid())
    os._exit(2)
else:
    while True:
        p,status = os.waitpid(-1,os.WNOHANG)      #结束子进程
        print('Child pid:',p)
        print('Child exit status:',status) #*256
        print('Child exit status:',os.WEXITSTATUS(status))
        if p != 0:
            break
        sleep(1)
    print('Parent process...')
    while True:
        pass