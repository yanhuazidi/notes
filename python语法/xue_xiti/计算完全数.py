   计算完全数　
 def wangquanshu(n):
     L1=[]
    x=1
     while x<x+1:
         L=[]
         for y in range(1,x//2+1):
             if x%y==0:
                 L.append(y)
         a=0
         for s in L:
            a+=s
         if a==x:
            L1.append(x)
        if len(L1)==n:
             return L1
        x+=1
 n=int(input('请输入要得到的完全数个数:'))
 print(wangquanshu(n))