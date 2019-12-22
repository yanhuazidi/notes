
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
    pid,status = os.wait()      #结束子进程
    print('Child pid:',pid)
    print('Child exit status:',status) #*256
    print('Child exit status:',os.WEXITSTATUS(status))
    print('Parent process...')
    while True:
        pass