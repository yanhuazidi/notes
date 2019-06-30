# import time
# def aaa():
#     print('你',end='',flush=True)
#     time.sleep(1)
#     print('是',end='',flush=True)
#     time.sleep(1)
#     print('谁',end='',flush=True)
#     time.sleep(1)
#     print('？',end='',flush=True)
#     time.sleep(1)
#     print('来',end='',flush=True)
#     time.sleep(1)
#     print('自',end='',flush=True)
#     time.sleep(2)
#     print('何',end='',flush=True)
#     time.sleep(2)
#     print('方',end='',flush=True)
#     time.sleep(2)
#     print('！')
# aaa()


print("1.")
def mymin(a,*arg):
    L=[y for y in a]
    m=L[0]
    for x in L:
        if m>x:
            m=x
    return m
print(mymin(1,2))

f=open("/home/tarena/test/aaa.mp3")
f1=f.read()
print(f1)
for x in f:
    print(x,end='')
f.close()