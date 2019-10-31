def gong(x,y):
    while y:
        t = x%y
        x,y = y,t
    return x
print(gong(4,6))