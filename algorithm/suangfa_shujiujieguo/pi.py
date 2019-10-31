#coding:utf-8

from fengshu import FengShu

L = [FengShu(4,x) for x in range(1,200004,2)]
i = 0
pi1 = FengShu(0,1)
pi2 = FengShu(0,1)
while i<=300:
    pi1+=L[i]
    pi2-=L[i+1]
    i+=2
pi = pi1+pi2
print(pi)
print(float(pi))
