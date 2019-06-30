print("十进制转二进制")
def mybin(_int):
    if _int == 0:
        return 0
    L = []
    result = ''
    while _int:
        wei = _int % 2
        _int //= 2
        L.append(wei)
    while L:
        result += str(L.pop())
    return result
try:
    m = int(input("输入整数:"))
except:
    print("傻")
    quit()
if m <0:
    m=abs(m)
    print('-0b',mybin(m))
else:
    print("0b",mybin(m))


print("十进制转二进制")
# def diguibin(_int,L):
#     if _int == 1:
#         L.append(_int%2)
#         return reversed(L)
#     L.append(_int%2)
#     return diguibin(_int // 2,L)
# binL=[]
# s=''
# for x in diguibin(5,binL):
#     s+=str(x)
# print("0b",s)

print("2")
def diguibin(n):
    if n:
        s = str(n % 2)
        return str(diguibin(n//2))+s
    else:
        return "0b"
print(diguibin(5))