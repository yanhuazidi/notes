
递归的基本原理：


１　每一次函数调用都会有一次返回．当程序流执行到某一级递归的结尾处时，它会转移到前一级递归继续执行．

２　递归函数中，位于递归调用前的语句和各级被调函数具有相同的顺序．如打印语句 #1 位于递归调用语句前，它按照递
　　归调用的顺序被执行了 4 次．

３　每一级的函数调用都有自己的私有变量．

４　递归函数中，位于递归调用语句后的语句的执行顺序和各个被调用函数的顺序相反．

５　虽然每一级递归有自己的变量，但是函数代码并不会得到复制．

６　递归函数中必须包含可以终止递归调用的语句．

print("判断回文")
def hui(s,end,start=0):
    if s[start]!=s[end]:
        return "不是回文"
    if start > end:
        return "是回文"
    return hui(s,end-1,start+1)
s = input("判断回文:")
s1=len(s)-1
print(hui(s,s1))

print("求第5人的年龄")
def year(x):
    if x==1:
        return 10
    return year(x-1)+2
print(str(year(5)))

#　　递归函数
def fn(n):
    if n==1:
        return 1
    return n*fn(n-1)
print(fn(20))

def fn(n):
    return fn_iter(1,1,n)
def fn_iter(x,count,n):
    if count>n:
        y=x
        return y
    return fn_iter(x*count,count+1,n)
print(fn(3))

print("十进制转二进制")
def diguibin(_int,L):
    if _int == 1:
        L.append(_int%2)
        return reversed(L)
    L.append(_int%2)
    return diguibin(_int // 2,L)
binL=[]
s=''
for x in diguibin(5,binL):
    s+=str(x)
print("0b",s)

print("2")
def diguibin(n):
    if n:
        s = str(n % 2)
        return str(diguibin(n//2))+s
    else:
        return "0b"
print(diguibin(5))

def fib(n):
    if n<=2:
        return 1
    return fib(n-2)+fib(n-1)