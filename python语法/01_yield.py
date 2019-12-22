def f1():
    for i in range(3):
        yield i 
    
g = f1()
for m in g:
    print(m)












