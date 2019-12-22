# #  第一章
# print('1.')
# name = input("请输人姓名:")
# print("你好！",name,"^-^",sep='')

# print('2.')
# try:
#     num = int(input("请输入数字:"))
# except:
#     print("你大爷好丑！")
#     exit()
# if 0<num<100:
#     print("你妹好漂亮!")
# else:
#     print("你大爷好丑！")

# print("3.")
# print("\\")
# print(r'\')　　报错

# ##    第二章
# print("1.")
# print(2**3**10)   算了

# print("2.")
# try:
#     year = int(input("请输入年份:"))
#     assert year>0
# except:
#     print("你是不是傻")
#     quit()
# if year%4==0 and year%100!=0 or year%400==0:
#     print(year,"年是润年")
# else:
#     print(year,"年不是润年")

# print("3.")
# for x in [y for y in range(100) if y%2==1]:
#     print(x,end=' ')
# print()

# print("4.")
# x=7
# while True:
#     if x%2==1 and x%3==2 and x%5==4 and x%6==5:
#         print(x)
#         break
#     else:
#         x+=7

## 第三章
# print("1.")
# try:
#     num = int(input("请输入整数:"))
# except:
#     print("是不是傻")
#     quit()
# print(bin(num))
# print(oct(num))
# print(hex(num))

# def shu(mima):
#     a=b=c = 0
#     for x in mima:
#         if x.isdigit():
#             a+=1
#         elif x.isalpha():
#             b+=1
#         else:
#             c+=1
#     return a,b,c
# mima = input("请输入密码:")
# a,b,c = shu(mima)
# if a>0 and b>0 and c>0 and len(mima)>16 and mima[0].isalpha():
#     print('高级密码')
# elif a>0 and b>0 or b>0 and c>0 or a>0 and c>0:
#     if len(mima)>8:
#         print("中级密码")
#     else:
#         print("低级密码")
# elif mima!='':
#     print("低级密码")
# else:
#     print("密码不合格")

##　　第四章
# print("1.")
# def mymin(a,*arg):
#     L=[y for y in a]
#     m=L[0]
#     for x in L:
#         if m>x:
#             m=x
#     return m
# print(mymin(1,2))

# print("2.")
# # def xulie(a,d):
# #     return a,d
# L= [1,2,3,4,5]
# L1 = ["a","b","c","d","e"]
# L3=[y for x in zip(L,L1) for y in x]
# print(L3)

# print("3.")
# try:
#     score = int(input("请输入成绩:"))
#     assert 0<=score<=100
# except:
#     print("傻")
#     quit()
# if 60<=score<80:
#     print("c")
# elif 80<=score<90:
#     print("b")
# elif 90<=score<+100:
#     print("a")
# else:
#     print('d')

# print("4.")
# x,y,z=6,5,4
# small=z if z<y else y if x>y else x if x<z else z
# print(small)

## 第五章
# print("求球的颜色搭配")
# for red in range(1,4):
#     for yellow in range(1,4):
#         for green in range(1,7):
#             if red+yellow+green==8:
#                 print(red,"红",yellow,"黄",green,"绿")
# print("求水仙花数")
# for x in range(100,1000):
#     _sum = 0
#     _x = x
#     while _x:
#         _sum = _sum +(_x%10)**3
#         _x//=10
#     if _sum == x:
#         print(x)

##　第六章
# print("十进制转二进制")
# def mybin(_int):
#     if _int == 0:
#         return 0
#     L = []
#     result = ''
#     while _int:
#         wei = _int % 2
#         _int //= 2
#         L.append(wei)
#     while L:
#         result += str(L.pop())
#     return result
# try:
#     m = int(input("输入整数:"))
# except:
#     print("傻")
#     quit()
# if m <0:
#     m=abs(m)
#     print('-0b',mybin(m))
# else:
#     print("0b",mybin(m))

# print("2.")
# def mypow(x,y):
#     return x**y
# print(mypow(3,3))

# print("3.")
# def gong(x,y):
#     while y:
#         t = x%y
#         x,y = y,t
#     return x
# print(gong(4,6))

### 第七章
# print("1.")
# def hui(s,end,start=0):
#     if s[start]!=s[end]:
#         return "不是回文"
#     if start > end:
#         return "是回文"
#     return hui(s,end-1,start+1)
# s = input("判断回文:")
# s1=len(s)-1
# print(hui(s,s1))

# print("2.")
# def year(x):
#     if x==1:
#         return 10
#     return year(x-1)+2
# print(str(year(5)))

# print("3.")
# def get_digits(s):
#     print(list(int(x)for x in (str(s))))
# get_digits(12345)

# print("4.")
# def diguibin(n):
#     if n:
#         s = str(n % 2)
#         return str(diguibin(n//2))+s
#     else:
#         return "0b"
# print(diguibin(5))

##　　第十章
# f=open("/home/tarena/test/aaa.mp3")
# f1 =open("/home/tarena/test/aaa.txt","x")
# f1.write(f.read())
# f.close()
# f1.close()

## 第十一章
# print("2.")
# def file_bijiao(file1,file2):
#     f1 = open(file1)
#     f2 = open(file2)
#     L =list(map(lambda x,y:x!=y,f1,f2))
#     L =[x for x in enumerate(L,1) if True in x]
#     return L
# file1 = input("请输入比较文件:")
# file2 = input("请输入被比较文件:")
# L = file_bijiao(file1,file2)
# print("您比较的文件有%d处不同"%len(L))
# for x,y in L:
#     print("第%d行不一样"%x)

# print("2.")
# def han(file_,n):
#     f = open(file_)
#     it = iter(f)
#     f.close()
#     while n>0:
#         print(next(it),end = '')
#         n-= 1
# file_ = input("请输入文件名:")
# n = int(input("请输入行:"))
# han(file_,n)

# print("3.")
# def shuchuhan(file_,start=0,end=0):
#     f = open(file_)
#     L=list(f)
#     f.close()
#     if end == 0:
#         end = len(L)
#     for x in L[start:end]:
#         print(x,end = '')
# file_ = input("请输入文件名:")
# start = int(input("请输入行:"))
# end = int(input("请输入行:"))
# shuchuhan(file_,start,end)

# print("4.")
# def replace(file_,new,old):
#     f = open(file_)
#     L = list(f)
#     f.close()
#     s = ''.join(L)
#     count = s.count(old)
#     print("文件中共有%d处要替换"%count)
#     m = input("您是否选择用%s替换%s(y):"%(new,old))
#     if m == 'y':
#         se = s.replace(old,new)
#         f = open(file_,'wt')
#         f.write(se)
#         f.close()
#         print("替换成功")
# file_ = input('请输入文件名:')
# old = input("请输入要替换的字符:")
# new = input("请输入替换的字符:")
# replace(file_,new,old)

# print("5.")
# def save():
#     file_ = input("请输入文件名:")
#     print("单行输入‘w’退出输入")
#     f = open(file_,'wt')
#     i = 1
#     while True:
#         word = input('%d :'%i)
#         if word == 'w':
#             break
#         f.write("%d %s\n"%(i,word))
#         i += 1
#     f.close()
# save()

##　　第十二章
# print("1.")
# import os
# all_files = os.listdir(os.curdir)
# type_dict = dict()

# for each_file in all_files:
#     if os.path.isdir(each_file):
#         type_dict.setdefault('文件夹',0)
#         type_dict['文件夹'] += 1
#     else:
#         ext = os.path.splitext(each_file)[1]
#         type_dict.setdefault(ext,0)
#         type_dict[ext] += 1
# for each_type in type_dict:
#     print("该文件夹下共有%s的文件%d个"%(each_type,type_dict[each_type]))

# print("2.")
# import os
# all_files = os.listdir(os.curdir)
# file_dict = {}
# for esch_file in all_files:
#     file_size = os.path.getsize(esch_file)
#     file_dict[esch_file] = file_size
# for each in file_dict.items():
#     print("%s文件的大小为%dbytes"%(each[0],each[1]))

# print("3.")
# import os
# def search_file(start_dir,target):
#     os.chdir(start_dir)
#     for each_file in os.listdir(os.curdir):
#         if each_file == target :
#             print(os.getcwd() + os.sep + each_file)
#         if os.path.isdir(each_file):
#             search_file(each_file,target)
#             os.chdir(os.pardir)
# start_dir = input("请输入开始目录:")
# target = input("请输入要查找的文件:")
# search_file(start_dir,target)

# print("4.")
# import os
# def search_file(start_dir,target):
#     os.chdir(start_dir)
#     for each_file in os.listdir(os.curdir):
#         ext = os.path.splitext(each_file)[1]
#         if ext in target:
#             L.append(os.getcwd()+os.sep+each_file+os.linesep)
#         if os.path.isdir(each_file):
#             search_file(each_file,target)
#             os.chdir(os.pardir)
# start_dir = input("请输入要查找的初始目录:")
# program_dir = os.getcwd()

# target = ['.py']
# L = []
# search_file(start_dir,target)
# f = open(program_dir + os.sep +'L.txt','w')
# f.writelines(L)
# f.close()

# print("5.")
# import os
# def print_pos(key_dict):
#     keys = key_dict.keys()
#     keys = sorted(keys)
#     for each_key in keys:
#         print("关键字出现在第%s行,第%s个位置."%(each_key,str(key_dict[each_key])))
# def pos_in_line(line,key):
#     pos = []
#     begin = line.find(key)
#     while begin != -1:
#         pos.append(begin + 1)
#         begin = line.find(key,begin+1)
#     return pos
# def search_in_file(file_name,key):
#     f = open(file_name)
#     count = 0
#     key_dict = dict()
#     for each_line in f:
#         count +=1
#         if key in each_line:
#             pos = pos_in_line(each_line,key)
#             key_dict[count] = pos
#     f.close()
#     return key_dict
# def search_files(key,detail):
#     all_files = os.walk(os.getcwd())
#     txt_files = []
#     for i in all_files:
#         for each_file in i[2]:
#             if os.path.splitext(each_file)[1] == '.txt':
#                 each_file = os.path.join(i[0],each_file)
#                 txt_files.append(each_file)
#     for each_txt_file in txt_files:
#         key_dict = search_in_file(each_txt_file,key)
#         if key_dict:
#             print('=================================================')
#             print('在文件%s中找到关键字%s'%(each_txt_file,key))
#             if detail in ['YES','Yes','yes']:
#                 print_pos(key_dict)
# key = input('请将该脚本放于待查找的文件夹内，请输入关键字：')
# detail = input('请问是否需要打印关键字%s在文件中的具体位置(yes/no):'%key)
# search_files(key,detail)

##  第十四章

# print('1.')
# class ju:
#     width = 4
#     length = 5
#     def setRect(self):
#         print("请输入矩形的长和宽")
#         self.width = float(input("长:"))
#         self.length = float(input("宽:"))
#     def get_ju(self):
#         print("宽和长为%f,%f"%(self.width,self.length))
#     def get_Aect(self):
#         return self.width*self.length
# a = ju()
# b = a.get_ju()

# print("3.")
# import random as r
# legal_x = [0,10]
# legal_y = [0,10]
# class Sparrow:
#     def __init__(self):
#         self.power = 100
#         self.x = r.randint(legal_x[0],legal_x[1])
#         self.y = r.randint(legal_y[0],legal_y[1])
#     def move(self): 
#         new_x = self.x + r.choice([1,2,-1,-2])
#         new_y = self.y + r.choice([1,2,-1,-2])
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#         self.power -= 1
#         return (self.x,self.y)
#     def eat(self):
#         self.power += 20
#         if self.power > 100:
#             self.power = 100
# class Parrot:
#     def __init__(self):
#         self.x = r.randint(legal_x[0],legal_x[1])
#         self.y = r.randint(legal_y[0],legal_y[1])
#     def move(self): 
#         new_x = self.x + r.choice([1,-1])
#         new_y = self.y + r.choice([1,-1])
#         if new_x < legal_x[0]:
#             self.x = legal_x[0] - (new_x - legal_x[0])
#         elif new_x > legal_x[1]:
#             self.x = legal_x[1] - (new_x - legal_x[1])
#         else:
#             self.x = new_x
#         if new_y < legal_y[0]:
#             self.y = legal_y[0] - (new_y - legal_y[0])
#         elif new_y > legal_y[1]:
#             self.y = legal_y[1] - (new_y - legal_y[1])
#         else:
#             self.y = new_y
#         return (self.x,self.y)
# turtle = Sparrow()
# parrot = []
# for i in range(10):
#     new_fish = Parrot()
#     parrot.append(new_fish)
# while True:
#     if not len(parrot):
#         print("鹦鹉被吃完了")
#         break
#     if not turtle.power:
#         print("麻雀体力耗尽")
#         break
#     pos = turtle.move()
#     for each_parrot in parrot[:]:
#         if each_parrot.move() == pos:
#             turtle.eat()
#             parrot.remove(each_parrot)
#             print("有一只鹦鹉被吃了")

# print("4.")
# class piaojia:
#     def __init__(self,weekend = False,child = False):
#         self.exp = 100
#         if weekend:
#             self.inc = 1.2
#         else:
#             self.inc = 1
#         if child:
#             self.childinc = 0.5
#         else:
#             self.childinc = 1
#     def manoy(self,d):
#         return self.exp*self.childinc*self.inc*d
# dar = piaojia()
# haiz = piaojia(child=True)
# print(dar.manoy(2)+haiz.manoy(1))

