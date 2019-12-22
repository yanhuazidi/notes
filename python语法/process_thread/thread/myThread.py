from threading import Thread
from time import ctime,sleep


class MyThread(Thread):
    def __init__(self,target,args=(),kwargs={},name='thread-1'):
        super().__init__()
        self.fun = target
        self.args = args
        self.kwargs = kwargs
        self.name = name
    
    def run(self):
        self.fun(*self.args,**self.kwargs)
        
        


if __name__=="__main__":

    def player(sec,song):
        for i in range(2):
            print("Playing %s:%s"%(song,ctime()))
            sleep(sec)
    t = MyThread(target=player,args=(3,),\
        kwargs={'song':'凉凉'},name='hehe')

    t.start()
    t.join()