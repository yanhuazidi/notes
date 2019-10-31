

# begin=int(input('input:'))
# end=int(input('input:'))
# while begin<=end:
#     print(begin,end=' ')
#     begin +=1
# print('\n\n','五个一行：',end='')

# begin=int(input('input:'))
# end=int(input('input:'))
# i=1
# while begin<=end:
#     print(begin,end=' ')
#     begin +=1
#     if i%5==0:
#         print()
#     i +=1
# print()

# w=int(input('请输入宽度:'))
# line=1
# while line<=w:
#     i=1
#     while i<=w:
#         print(i,end='')
#         i +=1
#     print()
#     line +=1

# ##　for语句　＃＃＃count功能
# str=input('请输入字符串:')
# i=0
# j=0
# for s in str:
#     if s=='a':
#         i +=1
#     if s==" ":
#         j +=1
# print(i,j)

## range 的for运用
# for s in range(1,21):
#     print(s,end=' ')
# print('\n')
# for w in range(1,21):
#     str(w)
#     print('%-3s'%(w),end=' ')
#     if w%5==0:
#         print()

##  练习　　＃＃＃
# print('满足的数有:',end='')
# for s in range(1,101):
#     if s*(s+1)%11==8:
#         print(s,end=' ')
# print()

# i=0
# cn=input('请输入一段字符:')
# for s in cn:
#     if ord(s)>127:
#         i +=1
# print(i)

##range函数会先执行并返回一个定值，range函数只调用一次
# i=6
# for x in range(1,i):
#     print('x=',x,'i=',i)
#     i-=1

# for c in range(65,91):
#     print(chr(c),end='')
# print()
# for b in range(97,123):
#     print(chr(b),end='')
# print()

# ##习题
# begin=int(input('begin:'))
# end=int(input('end:'))
# for s in range(begin,end):
#     if s%2==0:
#         continue
#     print(s,end=' ')
# print()

# print('第二题')
# he=0
# for s in range(1,101):
#     if s%2!=0 and s%3!=0 and s%5!=0 and s%7!=0:
#         print(s,end=' ')
#         he +=s
# print()
# print('和是:',he)


# L=[]
# while 1:
#     l=int(input("请输入:"))
#     if l<0:
#         break
#     L +=[l]
# print(L)

####练习＃＃＃＃
# print('练习一')
# m=int(input('请输入一个正整数:'))
# i=1
# while d<=m:
#     print('* '*d)
#     d +=1
# print()
# d=1
#     print('  '*(m-i),' *'*i,sep='')
#     i +=1
# print()
# i=1
# while i<=m:
#     print('* '*(m-i+1))
#     i +=1
# print()
# i=1
# while i<=m:
#     print('  '*(i-1),'* '*(m-i+1),sep='')
#     i +=1
# print()
# print('练习二')
# print("输入０结束")
# while 1:
#     m=int(input('请输入一个正整数:'))
#     for n in range(2,m):
#         if m%n==0:
#             print('这不是素数')
#             break

#     if m==0:
#         break
# print('练习三')
# Sn=0
# W=[]
# j=[]
# ja=[]
# i=1
# while i<=1000000:
#     W+=[1/(i*2-1)]
#     i +=1
# j=W[::2]
# ja=W[1::2]
# for s in j:
#     Sn+=s
# for y in ja:
#     Sn-=y
# print(Sn)
# ji=Sn*4
# print(ji)

# print('练习四')
# x=0
# i=0
# j=0
# g=0
# for s in range(100,999):
#     x=int(s/100)
#     i=s-x*100
#     j=int(i/10)
#     g=s-j*10-x*100
#     if x*x*x+j*j*j*+g*g*g==s:
#         print(s,'是水仙花数')
# print('or')
# for x in range(100,1000):
#     s=str(x)
#     bai=int(s[0])
#     shi=int(s[1])
#     ge=int(s[2])
#     if bai**3+shi**3+ge**3==x:
#         print(x,'是水仙花数')
# print('or')
# for b in range(1,10):
#     for s in range(0,10):
#         for g in range(0,10):
#             if b**3+s**3+g**3==b*100+s*10+g:
#                 print(b*100+s*10+g,'是水仙花数')
# print('or')
# for x in range(100,999):
#     b=x//100
#     s=x//10-b*10
#     g=x%10
#     if b**3+s**3+g**3==x:
#         print(x,'是水仙花数')


##　　周考　　　＃＃＃
# for s in range(100,999):
#     if s==(s//100)**3=(s//10-s//10)

# y=1
# while y<=9:
#     x=1
#     while x<=y:
#         print('%d*%d=%-2d'%(y,x,x*y),end=' ')
#         x+=1
#     print()
#     y +=1
# print('or')
# for y in range(1,10):
#     for x in range(1,y+1):
#         print('%d*%d=%-2d'%(y,x,x*y),end=' ')
#         if y==x:
#             print()

        



# m=int(input('输入１～１２７整数'))
# a=chr(m)
# print(a)

# for s in range(1,100):
#     if s%3==0 and s%5==0:
#         print(s)

# m=int(input('请输入金额:'))
# if 50<=m<=100:
#     print(r'折扣为%10')
#     print('应付:',m-m/10)
# elif m>100:
#     print(r'折扣为%20')
#     print('应付:',m-m/20)
# else:
#     print('不打折')


# s=input('input a string:')
# _alpha=0
# space=0
# digit=0
# others=0
# for c in s:
#     if c.isalpha():
#         _alpha+=1
#     elif c.isspace():
#         space+=1
#     elif c.isdigit():
#         digit+=1
#     else:
#         others+=1
# print('char=%d,space=%d,digit=%d,other=%d'%(_alpha,
# space,digit,others))


# L=[3,5]
# L[:0]=[1,2]
# print(L)
# L[2:2]=[4]
# print(L)
# L[5:]=[6]
# print(L)
# L=L[::-1]
# print(L)
# del L[-1]
# print(L)


# a=int(input('a='))
# b=int(input('b='))
# c=int(input('c='))
# L=[a,b,c]
# print('最大值:',max(L),'最小值:',min(L),'平均值:',(a+b+c)/3)
# print('\n\n')
# L=[]
# y=0
# print('输入－１结束')
# while 1:
#     x=int(input('请输入整数:'))
#     if x==-1:
#         break
#     L+=[x]
# print('共有:',len(L))
# print('最大为:',max(L))
# y=sum(L)/len(L)
# print('平均为:',y)


# print('one')
# begin=int(input('请输入一个整数:'))
# end=int(input('请输入一个整数:'))
# L=[x for x in range(begin,end) if x%2==0]
# print(L)

# print('two')
# print('输入０结束')
# L=[]
# while 1:
#     s=int(input('请输入整数:'))
#     if s==0:
#         break
#     L+=[s]
# L1=[x for x in L if x>0]
# L2=[x for x in L if x<0]
# print(L,L1,L2,sep='\n')

# s1='ABC'
# s2='123'
# L=[x+y for x in s1 for y in s2]
# print(L)

# s='100,200,300,500,800'
# L=[int(x) for x in s.split(',')]
# print(L)

# print('two')
# L=[x for x in range(1,101,3)]
# print(L)

# print('三')
# L=[[x,x+1,x+2] for x in range(1,8,3)]
# l=[[y for y in range(x,x+3)] for x in range(1,8,3)]
# print(L,'\n',l)

#练习＃＃＃
# print('输入０结束')
# L=[]
# L1=[]
# L2=[]
# while 1:
#     s=int(input('请输入一些数据:'))
#     if s==0:
#         break
#     L+=[s]
# for x in L:
#     if x not in L1:
#         L1+=[x]   
# print(L1)    
# for x in L:
#     if x not in L2 and L.count(x)==2:
#         L2.append(x)
# print(L2)

# print('二')
# L=[1]
# for m in range(1,100):
#     for n in range(2,m):
#         if m%n==0:
#             break
#     else:
#         L.append(m) 
# print(L)

# print('三')
# L=[]
# y1=1
# y=0
# while len(L)<40:
#     L+=[y1]
#     y2=y+y1
#     y=y1
#     y1=y2
# print(len(L))
# print(L)

# d={'name':'tarena','age':15}
# d['address']='北京市海淀区'
# print(d)

# d={}
# d[1]='春季有１，２，３月'
# d[2]='春季有4，5，6月'
# d[3]='春季有7，8，9月'
# d[4]='春季有10，11，12月'

# while 1:
#     m=int(input('请输入一个整数:'))
#     if 0<m<5:
#         print(d[m])
#     else:
#         print('信息不存在')
#         break

# ##(1)
# s=input('请输入字符串:')
# d={}
# y=1
# for x in s:
#     if x in d:
#         d[x]+=1
#     else:
#         d[x]=1
# for k,v in d.items():
#     print(k,':',v,'次')
#(2)
# s=input('请输入字符串:')
# L = []
# for ch in s:
#     if ch not in L:
#         L.append(ch)
# for ch in L:
#     print(ch,":",s.count(ch),'次')

# L=['tarena','xiaozhang','hello']
# d={x: len(x) for x in L}
# print(d)

# # #　　　练习
# print('一.')
# L=['tom','jerry','spike','tyke']
# L1=[1001,1002,1003,1004]
# print('1.')
# print({L[x]:L1[x] for x in range(len(L))})
# print('2.')
# L2={}
# for s in range(len(L)):
#     L2.update({L[s]:L1[s]})
# print(L2)
# print('3.')
# L3={}
# for y in range(len(L)):
#     L3[L[y]]=L1[y]
# print(L3)

# def myadd(x,y):
#     s=x+y
#     print(s)
# myadd(100,200)
# myadd("ABC","123")

# def myadd2(x,y):
#     s=x+y
#     return s
# a=int(input('请输入第一个数:'))
# b=int(input('请输入第二个数:'))
# print('您输入的两个数之和为:',myadd2(a,b))

# def mymax3(a,b,c):
#     da=a
#     if da<b:
#         da=b
#     elif da<c:
#         da=c
#     return da

# print(mymax3(100,300,200))
# print(mymax3("ABC","123","abc"))

# L=[]
# b=0
# c=0
# d=0
# def input_numbers(L):
#     while 1:
#         a=int(input('请输入整数:'))
#         if a<0:
#             return L,b,c,d
#         L.append(a)
#         b=max(L)
#         c=min(L)
#         d=sum(L)
# L,b,c,d=input_numbers(L)
# print(L)
# print('用户输入的最大值是:',b)
# print('用户输入的最小值是:',c)
# print('用户输入的值之和是:',d)

# print('练习')
# print('一.')
# m=0
# def get_chinese_char_count(s):
#     y=0
#     for x in s:
#         if ord(x)>127:
#             y+=1
#     return y
# s=input('请输入中文混合的字符串:')
# m=get_chinese_char_count(s)
# print('您输入的中文字符个数是:',m)

# print('二．')
# def sum3(a,b,c):
#     return a+b+c
# def pow(x):
#     return x**3
# print('1.')
# x=sum3(pow(1),pow(2),pow(3))
# print(x)
# print('2.')
# y=pow(sum3(1,2,3)) 
# print(y)

# #十进制转二进制
# def shier(i):
#     def Lshier(_i):
#         L=[]
#         si=''
#         if _i==0 or _i==1:
#             L.append(_i)
#             for s in L:
#                 si+=str(s)
#             return si
#         while 1:
#             c=_i//2
#             y=0
#             y=_i%2
#             L+=[y]
#             if c>=2:
#                 _i=c
#                 continue
#             else:
#                 L+=[1]
#                 L1=L[::-1]
#                 for s in L1:
#                     si+=str(s)
#                 return si
#     y=i
#     if i<0:
#         i=abs(i)
#     ss=Lshier(i)
#     if y<0:
#         print('-0b',ss,sep='')
#     else:
#         print('0b',ss,sep='')
# m=int(input('输入整数:'))
# shier(m)
#####缺省参数
# def he(a=0,b=0,c=0,d=0):
#     tahe=a+b+c+d
#     return tahe
# print(he(10,20))
# print(he(100,200,300))
# print(he(1,2,3,4))   
# print(he(1))
# print(he())

# def myadd(*args):
#     he=0
#     for s in args:
#         he+=s
#     return he
# print(myadd())
# print(myadd(1,2,3,4,5,6,7,8,9))
# print(myadd(1,0,-6))

# def min_max(a,*rags):
#     l=[0,100]
#     t=min(a,*rags,*l),max(a,*rags,*l)
#     return t
# print(min_max(10,20,30))
# print(min_max(8,6,4,3,9,2,1))

# #range函数形参
# def myrange(start,stop=None,spet=1):
#     L=[]
#     if stop is None:
#         stop=start
#         start=0
#     for s in range(start,stop,spet):
#         L.append(s)
#     return L
# L=myrange(1,12,2)
# print(L)

### 练习
# print('一．')
# def isprime(x):
#     if x==1:
#         return True
#     for s in range(2,x):
#         if x%s==0:
#             return False
#     return True
# m=int(input('请输入一个正整数:'))
# print(isprime(m))
# print('\n')
# print('二．')
# def prime_m2n(m,n):
#     L1=[]
#     L=[s for s in range(m,n) for y in range(2,s) if s%y==0]
#     for x in range(m,n):
#         if x not in L:
#             L1.append(x)
#     return L1
# m=int(input('请输入一个正整数m:'))
# n=int(input('请输入一个大于m正整数n:'))
# L=prime_m2n(m,n)
# print(L)
# print('三.')
# def primes(n):
#     L1=[]
#     L=[s for s in range(1,n) for y in range(2,s) if s%y==0]
#     for x in range(1,n):
#         if x not in L:
#             L1.append(x)
#     return L1
# print('1.')
# print('100以内全部素数:\n',primes(100))
# print('2.')
# L=primes(200)
# s=0
# for x in L:
#     s +=x
# print('200以内素数的和是：',s)  

# print('四.')
# def input_student():
#     L=[]
#     while True:
#         name=input('学生姓名:')
#         if name=='':
#             break
#         age=int(input('学生年龄:'))
#         score=int(input('学生成绩:'))
#         d={'name':name,'age':age,'score':score}
#         L.append(d)
#     return L
# def print_student():
#     L=input_student()
#     print('+','-'*8,'+','-'*7,'+','-'*7,'+',sep='')
#     print('|','name'.center(8),'|','age'.center(7),'|','score'.center(7),'|',sep='')
#     print('+','-'*8,'+','-'*7,'+','-'*7,'+',sep='')
#     for x in range(0,len(L)):
#         b=L[x]
#         s1,s2,s3='%s'%b['name'],'%d'%b['age'],'%d'%b['score']
#         print('|',s1.center(8),'|',s2.center(7),'|',s3.center(7),'|',sep='')
#         print('+','-'*8,'+','-'*7,'+','-'*7,'+',sep='')
# print_student()

# #     全局声明
# count=0
# def hello(name):
#     print('你好:',name)
#     global count
#     count+=1
# hello('Tom')
# hello('Jerry')
# print('hello函数被调用%d次'%count)


# fx=lambda n:(n**2+1)%5==0
# print(fx(3))
# print(fx(4))

# mymax=lambda x,y:max(x,y)
# print(mymax(100,200))
# print(mymax('ABC','123'))

# ##   杨辉三角
# def shuanfa(n):   
#     for x in range(1,n+1):
#         L=[]
#         for y in range(1,x+1):
#             if y==1 or y==x:
#                 L+=[1]
#             else:
#                 a=L1[y-2]+L1[y-1]
#                 L+=[a]
#         L1=L
#         s=shuchu(L)
# def shuchu(L):
#     L1=[]
#     for x in L:
#         L1.append(str(x))
#     s=' '.join(L1)
#     w=n*3
#     print(s.center(w))
# n=int(input('请输入杨辉三角层数:'))
# shuanfa(n)

# def yh_1(L):    #   L 为上一行列表
#     d=[1]     #第一列　１
#     for i in range(len(L)-1):   # 从０～上一行长度－１ 
#         d.append(L[i]+L[i+1])　# 加入中间元素
#     d.append(1)　　　# 最后列　１
#     return d       #  返回 n 行列表
# def yh_2(n):
#     L=[]
#     d=[1]
#     for _ in range(n):
#         L.append(d)   # 
#         d=yh_1(d)     #将列表d传给Ｌ
#     return L
# def yh_3(L):                # 把列表转换为字符串
#     L2=[str(x) for x in L]
#     return ' '.join(L2)
# L=yh_2(7)       # 生成的嵌套列表
# zdhs=len(yh_3(L[-1]))  #把Ｌ最后元素传入函数yh_3,计算三角最长一行长度
# for x in L:　　　       #　循环输出
#     s=yh_3(x)
#     print(s.center(zdhs))


# ##   高阶函数 map函数的使用       
# def power2(x):
#     return x**2
# for s in map(power2,range(1,10)):
#     print(s)   #1,4,9,16,25,36,49,84,81

# for x in map(pow,range(1,5),range(4,0,-1)):
#     print(x)   #1,8,9,4

# ##  函数式编程应用
# print(sum(map(lambda x:x**2,range(1,10))))
# print(sum(map(lambda x:x**3,range(1,10))))
# print(sum(map(pow,range(1,10),range(9,0,-1))))
# L=map(pow,range(1,10),range(9,0,-1))
# print(L)
# print(sum(L))
# def aaa():
#     pass
# print(aaa)

#装饰器
# def mydeco(fn):
#     def fx():
#         print('++++++++++++')
#         fn()
#         print('------------')
#     return fx
# @mydeco
# def myfunc():
#     print('========')
# myfunc()

# ##　　随机模块
# from math import factorial as jiecheng
# n=int(input('输入整数:'))
# print(sum(map(jiecheng,range(1,n+1))))

# import random
# x=random.choice(range(1,100))
# i=0
# while True:
#     y=int(input('请输入一个数:'))
#     i+=1
#     if y==x:
#         print('恭喜你猜对了')
#         break
#     elif y>x:
#         print('你猜大了')
#     elif y<x:
#         print('你猜小了')
# print(i)

# import random
# y=int(input('请输入一个数:'))
# i=0
# while True:
#     x=random.choice(range(1,100))
#     i+=1
#     if x==y:
#         print('猜对了\n猜了:',i,'次')
#         break

# def fn():
#     while 1:
#         try:
#             m=int(input('m='))
#             n=int(input('n='))
#         except ValueError:
#             print('输入错误')
#             continue 
#         if m==0:
#             break
# fn() 

# def get_age():
#     try:
#         m=int(input('请输入年龄:'))
#     except ValueError:
#         raise ValueError('你好蠢，哈哈哈哈哈') 
#     if m<1 or m>140:
#         aaa=ValueError('你是不是傻,哈哈哈啊哈哈哈')
#         raise aaa
# get_age()

### yield　的使用
# def myeven(start,stop):
#     i=start
#     if i%2==0:
#         while i<stop:
#             i+=2
#             yield i
#     else:
#         i=i-1
#         while i<stop:
#             i+=2
#             yield i
# L=list(myeven(1,20))
# print(L)

# L=[2,3,5,7,10,15]
# def pinfan(L):
#     for x in L:
#         yield x**2+1
# it=iter(pinfan(L))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print()
# i3=iter(y**2+1 for y in L)
# print(next(i3))
# print(next(i3))
# print(next(i3))
# print(next(i3))
# print(next(i3))
# print(next(i3))
# L1=[z**2+1 for z in L]
# print(L1)

### enumerate 函数的使用
# L=[]
# while 1:
#     m=input('请输入:')
#     if m=='':
#         break
#     L.append(m)
# d={}
# for x,y in enumerate(L,1):
#     print('第',x ,'行:',y,sep='')
#     d.update({x:y})
# print(d)
# for z in d.items():
#     print(z)

# ba=bytearray(b'a1b2c3d4')
# b=bytes(ba[1:8:2])
# b1=bytes(ba[:7:2])
# print(b,'\n',b1)
# s=ba.decode('utf-8')
# st=s.upper()
# print(st)
# bba=st.encode('utf-8')
# print(bba)

# b=bytearray(b'aaaaa')
# print(b)
# print(id(b))
# del b[:3]
# print(b)
# print(id(b))

#      类
# class Dog:
#     '''此语句用来定义一个新的类型Dog'''
#     def eat(self,food):
#         '''此方法用来描述小狗吃的行为'''
#         print('id为%d的小狗正在吃%s'%(id(self),food))
#     def sleep(self,hour):
#         print('id为%d的小狗睡了%d小时'%(id(self),hour))
#     def play(self,w):
#         print('id为%d的小狗在玩%s'%(id(self),w))
# dog1=Dog()
# dog2=Dog()
# dog1.eat('骨头')
# dog2.eat('狗粮')
# print()
# dog1.sleep(1)
# dog2.sleep(2)
# print()
# dog1.play('球')
# dog2.play('猫')
# Dog.play(dog1,'球')　#当函数调用

# class Dog:
#     def eat(self,food):
#         print(self.color,'的',self.kinds,'正在吃',food)
#         self.last_food = food
#     def show_info(self):
#         print(self.color,"的",self.kinds,"上次吃的",self.last_food)
# dog1 = Dog()
# dog1.kinds = "哈士奇"
# dog1.color = "黑白相间"
# dog1.color = "白色"
# print(dog1.color,"的",dog1.kinds)
# dog1.eat('骨头')
# dog1.show_info()

# class Human:
#     def set_info(self,name,age,adress='不详'):
#         '''此方法用来给人对象添加姓名，年龄，地址'''
#         self.name = name
#         self.age = age
#         self.adress = adress
#         f = open('/home/tarena/aid1808/linux/human.txt','a')
#         f.write(name+' '+str(age)+' '+adress+'\n')
#         f.close()
#     def show_info(self):
#         '''显示此人信息'''
#         print('name:',self.name,'age:',self.age,'adress:',self.adress)
# s1 = Human()
# s1.set_info('小李',22,'北京')
# s2 = Human()
# s2.set_info('小赵',23,'上海')
# s1.show_info()
# s2.show_info()

# class car:
#     def __init__(self,c,b,m):
#         self.color = c
#         self.brand = b
#         self.model = m
#         print('初始化方法被调用')
#     def run(self,speed):
#         print(self.color,'的',self.brand,self.model,
#                 '正在以',speed,'公里／小时打速度行驶')
# a4 = car('红色','奥迪','A4')
# a4.run(100)

# class student:
#     def __init__(self,n,e,s = 0):
#         self.name = n
#         self.ega = e
#         self.score = s
#     def set_score(self,score):
#         self.score =score
#     def show_info(self):
#         print('姓名:'+self.name+' 年龄:'+str(self.ega)+' 成绩:'+str(self.score))

# L=[]
# L.append(student('小王',20,100))
# L.append(student('小李',19))
# L.append(student('小金',18,90))
# for x in L:
#     x.show_info()
# L[1].set_score(80)
# for y in L:
#     y.show_info()

# class car():
#     def __init__(self,info):
#         self.info = info
#         print("汽车",info,"对象被创建")
#     def __del__(self):
#         '''这是析构方法,形参只有一个self'''
#         print("汽车",self.info,"被销毁")
# c1 = car("BYD E6")
# input("press any key continue")
# print('end')

# class jir:
#     def __init__(self,name,ega):
#         self.name = name
#         self.ega = ega
#         self.qian = 0
#         self.skill = []

#     def teach(self,other,jineng):
#         print('\t',self.name,"教",other.name,jineng,sep='')
#         other.skill = jineng
#     def work(self,qian):
#         self.qian = qian
#     def borrow(self,jie,qian):
#         print('\t',self.name,'向',jie.name,"借了",qian,"元钱",sep='')
#         self.qian = qian
#         jie.qian = jie.qian - qian
#     def show_info(self):
#         print('\t',str(self.ega),'岁的',self.name,"有:",self.qian,"元钱"
#               ",他学会了",self.skill,sep='')
# m1 = jir('张三',35)
# m2 = jir('李四',8)
# m1.teach(m2,'python')
# m2.teach(m1,'王者荣耀')
# m1.work(1000)
# m2.borrow(m1,200)
# m1.show_info()
# m2.show_info()

# class Car:
#     total_count = 0
#     def __init__(self,info):
#         self.info = info
#         self.__class__.total_count+=1
#     def __del__(self):
#         self.__class__.total_count-=1
# c1 = Car("ＢＹＤ　Ｅ６")
# c2 = Car("吉利 E7")
# print("当前有%d个汽车对象"%Car.total_count)
# del c1
# print("当前有%d个汽车对象"%Car.total_count)

# class Human:
#     __slots__ = ['name','age']
#     def __init__(self,n,a):
#         self.name,self.age = n,a
#     def show_info(self):
#         print(self.name,self.age)

# class A:
#     @staticmethod
#     def myadd(a,b):
#         return a+b

# print(A.myadd(100,200))
# a = A()
# print(a.myadd(300,400))

# class Human:
#     '''此类用于描述人类的共性'''
#     def say(self,what):
#         print('说:',what)

#     def walk(self,distance):
#         print("走了",distance,"公里")
# h1 = Human()
# h1.say('天真蓝')
# h1.walk(5)

# class A:
#     def __init__(self):
#         self.__p1 = 100
#         print("self.__p1=",self.__p1)
#     def __m(self):
#         '''这是私有方法，此方法只能用此类的方法来调用
#         不能在其他地方调用'''
#         print("A.__m方法被调用")
#     def dowork(self):
#         '''此方法可以调用私有实例属性和方法'''
#         self.__m
# class B(A):
#     '''此类示意子类不能调用父类的私有成员'''
#     def test(self):
#         self.__m()  #报错
# a = A()
# print(a.__p1)  # 错误，不允许访问私有属性
# a.__m()        # 错误
# a.dowork()     # A.__m方法被调用

# class Shape:
#     def draw(self):
#         print("Shape.draw被调用")
# class Point(Shape):
#     def draw(self):
#         print("Point.draw被调用")
# class Circle(Point):
#     def draw(self):
#         print("Circle.draw被调用")
# def my_draw(s):
#     s.draw()    #此处显示出多态中的动态
# s1 = Circle()
# s2 = Point()
# my_draw(s2)
# my_draw(s1)

# class Car:
#     def fly(self,speed):
#         print("汽车以",speed,"km/h的速度行驶")
# class Plane:
#     def fly(self,height):
#         print("飞机以海拔",height,"米高度飞行")

# class PlaneCar(Plane,Car):
#     pass
# p1 = PlaneCar()
# p1.fly(10000)


# class A:
#     def __enter__(self):
#         print("已经进入")
#         return self
#     def __exit__(self,exc_t,exc_v,exc_tb):
#         '''exc_t用来绑定异常类型
#         exc_v用来绑定异常对象
#         exc_tb用来追踪对象
#         在没有异常时三个绑定None'''
#         if exc_t is None:
#             print("正常离开")
#         else:
#             print("异常离开")
# with A() as a:
#     print("这是with语句内部的语句")
#     int(input("请输入整数:"))

# class MyNumber:
#     def __init__(self,value):
#         self.data = value
#     def __repr__(self):
#         return '%d'%self.data
#     def __add__(self,rhs):
#         return self.data+rhs.data
#     def __sub__(self,rhs):
#         return self.data - rhs.data
# n1 = MyNumber(100)
# n2 = MyNumber(200)
# n3 = n1 + n2
# print(n1,'+',n2,"=",n3)
# n4 = n2 - n1
# print(n2,'-',n1,"=",n4)

# class MyList:
#     def __init__(self,n=()):
#         self.data =[x for x in n]
#         self.i = -1
#     def __repr__(self):
#         return 'MyList(%s)'%self.data
#     def __iter__(self):
#         return MyList(self)
#     def __next__(self):
#         self.i+=1
#         if self.i==len(self.data):
#             raise StopIteration
#         return self.data[i]
#     def __add__(self,other):
#         return MyList(self.data+other.data)
#     def __mul__(self,conut):
#         return MyList(self.data*conut)
#     def __rmul__(self,conut):
#         return MyList(self.data*conut)
# L1 = MyList(range(1,4))
# L2 = MyList([4,5,6])
# L3 = L1 + L2
# print(L3)
# L4 = L2 +L1
# print(L4)
# L5 = L1*3
# print(L5)
# L6 = 3*L1
# print(L6)

# b = r'''adfdsdf\n\vd
# fsfdf\
# fghfgh\nfhfg'''
# print(b)

# print('\n一.')
# for x in range(1,10):
#     for y in range(1,x+1):
#         print('%dx%d=%d'%(y,x,x*y),' ',end='')
#     print()

# print('\n二.')
# def myxrange(start=0,stop=None,step=1):
#     assert type(start)is int and type(stop)is int and type(step)is int,'输入不是整形!'
#     if stop==None:
#         start,stop=stop,start
#     if step<0:
#         if stop>=start:
#             yield []
#         while stop>start:
#             yield stop
#             stop+=step
#     elif step>0:
#         while start<stop:
#             yield start
#             start+=step
#     else:
#         raise ValueError
# print(sum(x**2 for x in myxrange(1,10)))
# print(sum(x**2 for x in range(1,10,2)))

# print('\n三．')
# def banduan(a):
#     if a <0:
#         return False
#     else:
#         return True
# def myfilter(fn,it):
#     for x in it:
#         if fn(x):
#             yield x
#         else:
#             continue
# L=[-1,-2,-3,1,2,3]
# L1=list(myfilter(banduan,L))
# print(L1)
# L2=list(filter(banduan,L))
# print(L2)


# def _copy(path1):
#     f=open(path1,'rb')
#     for x in f:
#         yield x
#     f.close()
# def _copy1(path2,x):
#     f=open(path2,'ab')
#     f.write(x)
#     f.close()
# str1=input('请输入文件所在:')
# str2=input('请输入复制位置:')
# for x in _copy(str1):
#     # x=x.decode()
#     _copy1(str2,x)

# class Fibonacci:
#     def __init__(self,n):
#         self.__shu=n
#         self.__i=-1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         self.__i+=1
#         if self.__i == self.__shu:
#             raise StopIteration
#         return self.fei()[self.__i]
#     def fei(self):
#         L=[]
#         x,y=0,1
#         while len(L)<=self.__shu:
#             z=x+y
#             x,y=y,z
#             L.append(x)
#         return L
# it = iter(Fibonacci(5))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# for x in Fibonacci(10):
#     print(x)
# print(sum(Fibonacci(10)))


# class car:
#     def __init__(self,c,b,m):
#         self.color = c
#         self.brand = b
#         self.model = m
#         self.__i = 3
#         print('初始化方法被调用')
#     def run(self,speed):
#         print(self.color,'的',self.brand,self.model,
#                 '正在以',speed,'公里／小时打速度行驶')
# class Car(car):
#     pass

# a4 = Car('红色','奥迪','A4')
# a4.run(100)
# print(a4.__i)
# a4.__dict__['__i'] = 10
# print(a4.__i)

# class car():
#     def __init__(self,info):
#         self.info = info
#         print("汽车",info,"对象被创建")
#     def __del__(self):
#         '''这是析构方法,形参只有一个self'''
#         print("汽车",self.info,"被销毁")
# c1 = car("BYD E6")
# input("press any key continue")
# print('end')

# class Car:
#     total_count = 0
#     print(total_count)
#     total_count +=100
#     print(total_count)
# c1 = Car()
# print(c1.total_count)
# Car.total_count = 5
# print(Car.__dict__['total_count'])
# c1.__class__.total_count = 9
# print(c1.total_count)
# c1.total_count = 88
# print(Car.total_count)

# class Shape:
#     def draw(self):
#         print("Shape.draw被调用")
# class Point(Shape):
#     def draw(self):
#         print("Point.draw被调用")
# class Circle(Point):
#     def draw(self):
#         print("Circle.draw被调用")
# def my_draw(s):
#     s.draw()    #此处显示出多态中的动态
# s1 = Circle()
# s2 = Point()
# my_draw(s1)    # Circle.draw被调用
# my_draw(s2)    # Point.draw被调用


# from math import factorial as jiecheng
# n=int(input('输入整数:'))
# print(sum(map(jiecheng,range(1,n+1))))

# print('3.')
# L=[[3,5,8],10,[[13,14],15,18],20]
# l=[]
# def yi(L):
#     for x in L:
#         if type(x) is list:
#             yi(x)
#         else:
#             l.append(x)
#     return l
# print(yi(L))
# print(sum(l))

# def fn(n=1000,*args,a=100):
#     print(*args,a)
# fn(2,3,4,5,6)

# import time,sys
# L=['年:','月：','日:']
# L1=[]
# for x in L:
#     m=int(input(x))
#     L1.append(m)
# print(L1)
# L1=L1+[0,0,0,0,0,0]
# print(L1)
# sys.exit(0)
# print(L1)
# print(L1)

# print('1.')
# import math
# def fun(n):
#     print(sum([1/x for x in map(math.factorial,range(n+1))]))
# fun(int(input('请输入:')))
# print(math.log(10000,2))

# import random
# s={'\u2660'' A','\u2663'' A','\u2665'' A','\u2666'' A',
# '\u2660'' 2','\u2663'' 2','\u2665'' 2','\u2666'' 2',
# '\u2660'' 3','\u2663'' 3','\u2665'' 3','\u2666'' 3',
# '\u2660'' 4','\u2663'' 4','\u2665'' 4','\u2666'' 4',
# '\u2660'' 5','\u2663'' 5','\u2665'' 5','\u2666'' 5',
# '\u2660'' 6','\u2663'' 6','\u2665'' 6','\u2666'' 6',
# '\u2660'' 7','\u2663'' 7','\u2665'' 7','\u2666'' 7',
# '\u2660'' 8','\u2663'' 8','\u2665'' 8','\u2666'' 8',
# '\u2660'' 9','\u2663'' 9','\u2665'' 9','\u2666'' 9',
# '\u2660'' 10','\u2663'' 10','\u2665'' 10','\u2666'' 10',
# '\u2660'' J','\u2663'' J','\u2665'' J','\u2666'' J',
# '\u2660'' Q','\u2663'' Q','\u2665'' Q','\u2666'' Q',
# '\u2660'' K','\u2663'' K','\u2665'' K','\u2666'' K',
# '大王','小王'}
# s1=set(random.sample(s,17))
# s2=set(random.sample((s-s1),17))
# s3=set(random.sample((s-s1-s2),17))
# s4=s-s1-s2-s3
# print('第一个人持牌为:',s1)
# print('第二个人持牌为:',s2)
# print('第三个人持牌为:',s3)
# print('底牌为:',s4)

# s={'唐僧','悟空','八戒','沙僧'}
# it=iter(s)
# print(it)
# while 1:
#     try:
#         print(next(it))
#     except StopIteration:
#         break

##　9.20　　号练习
# def qiu(n,i):
#     if i==10:
#         print(n)
#         return 100
#     return qiu(n/2,i+1)+n
# print(qiu(100,0))

# print('2.')
# def fenjie(n,L):
#     for x in range(2,n+1):
#         if n%x==0:
#             L.append(x)
#             if x==n:
#                 a=1
#                 for y in L:
#                     a*=y
#                 b='*'.join([str(x) for x in L])
#                 print(a,'=',b)
#             else:
#                 fenjie(n//x,L)
#                 break
#         continue
# m=int(input('请输入一个正整数:'))
# L=[]
# fenjie(m,L)

# def fenjie(n,L):
#     for x in range(2,n+1):
#         if n%x==0:
#             L.append(x)
#             if n==x:
#                 return L
#             return fenjie(n//x,L)
# m=int(input('请输入一个正整数:'))
# L=[]
# b='*'.join([str(x) for x in fenjie(m,L)])
# print(m,'=',b)

# class MyNumber:
#     def __init__(self,value):
#         self.data = value
#     def __str__(self):
#         return "数字%d"%self.data

# n1 = MyNumber(100)
# s1 = str(n1)
# s2 = repr(n1)
# print(s1)
# print(s2)

# class MyList:
#     def __init__(self,iterable=()):
#         self.data = [x for x in iterable]
#     def __str__(self):
#         return 'eeeeeee'
# myl = MyList([1,-2,3,-4])
# print(str(myl))