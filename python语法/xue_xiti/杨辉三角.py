
def shuanfa(n):   
    for x in range(1,n+1):
        L=[]
        for y in range(1,x+1):
            if y==1 or y==x:
                L+=[1]
            else:
                a=L1[y-2]+L1[y-1]
                L+=[a]
        L1=L
        s=shuchu(L)
def shuchu(L):
    L1=[]
    for x in L:
        L1.append(str(x))
    s=' '.join(L1)
    w=n*3
    print(s.center(w))
n=int(input('????????????????:'))
shuanfa(n)

def yh_1(L):
    d=[1]
    for i in range(len(L)-1):
        d.append(L[i]+L[i+1])
    d.append(1)
    return d
def yh_2(n):
    L=[]
    d=[1]
    for _ in range(n):
        L.append(d)
        d=yh_1(d)
    return L
def yh_3(L):
    L2=[str(x) for x in L]
    return ' '.join(L2)
L=yh_2(7)
zdhs=len(yh_3(L[-1]))
for x in L:
    s=yh_3(x)
    print(s.center(zdhs))