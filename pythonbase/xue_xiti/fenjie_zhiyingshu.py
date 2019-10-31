def fenjie(n,L):
    for x in range(2,n+1):
        if n%x==0:
            L.append(x)
            if x==n:
                return L
            return fenjie(n//x,L)
m=int(input('请输入一个正整数:'))
L=[]
b='*'.join([str(x) for x in fenjie(m,L)])
print(m,'=',b)