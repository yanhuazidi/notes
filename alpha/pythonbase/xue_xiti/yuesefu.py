n = int(input("人数:"))
k = int(input("第几人开始:"))
m = int(input("第几个数出局:"))
L =list(range(1,n+1))
Lx = []
while L: 
    L = L[k-1:] + L[:k-1]
    k = m
    if m >len(L):
        m = m-len(L)
    Lx.append(L.pop(m-1))
print(Lx)