
百位三次方+十位三次方+个位三次方==原数
x=0
i=0
j=0
g=0
for s in range(100,999):
    x=int(s/100)
    i=s-x*100
    j=int(i/10)
    g=s-j*10-x*100
    if x*x*x+j*j*j*+g*g*g==s:
        print(s,'是水仙花数')

print('2.')
for x in range(100,1000):
    s=str(x)
    bai=int(s[0])
    shi=int(s[1])
    ge=int(s[2])
    if bai**3+shi**3+ge**3==x:
        print(x,'是水仙花数')

print('3.')
for b in range(1,10):
    for s in range(0,10):
        for g in range(0,10):
            if b**3+s**3+g**3==b*100+s*10+g:
                print(b*100+s*10+g,'是水仙花数')
print('or')
for x in range(100,999):
    b=x//100
    s=x//10-b*10
    g=x%10
    if b**3+s**3+g**3==x:
        print(x,'是水仙花数'

print("求水仙花数")              
for x in range(100,1000):
    _sum = 0
    _x = x
    while _x:
        _sum = _sum +(_x%10)**3
        _x//=10
    if _sum == x:
        print(x)