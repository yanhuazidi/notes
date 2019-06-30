（计算输入字符串的成分个数）
s=input('input a string:')
_alpha=0
space=0
digit=0
others=0
for c in s:
    if c.isalpha():
        _alpha+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1
print('char=%d,space=%d,digit=%d,other=%d'%(_alpha,
space,digit,others))