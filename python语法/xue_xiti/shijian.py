
def naozhong():
    import time
    L=['时:','分:','秒:']
    L1=[]
    print('设定闹钟')
    for x in L:
        jiesu=int(input(x))
        L1.append(jiesu)
    while True:
        y=time.localtime(time.time())[0]
        m=time.localtime(time.time())[1]
        d=time.localtime(time.time())[2]
        h=time.localtime(time.time())[3]
        f=time.localtime(time.time())[4]
        s=time.localtime(time.time())[5]
        print(' %02d:%02d:%02d:%02d:%02d:%02d'%(y,m,d,h,f,s),end='\r')
        L2=[h,f,s]
        if L2==L1:
            break
        time.sleep(1)
    print('滴答滴答滴答滴答')

def jishiqi():
    import time
    L=['时:','分:','秒:']
    L1=[]
    print('设定时间')
    for x in L:
        jiesu=int(input(x))
        L1.append(jiesu)
    s=0
    while True:
        time.sleep(1)
        s+=1
        T=time.gmtime(s)
        print(' %02d:%02d:%02d'%(T[3],T[4],T[5]),end='\r')
        L2=[T[3],T[4],T[5]]
        if L1==L2:
            print('时间到了')
            break
