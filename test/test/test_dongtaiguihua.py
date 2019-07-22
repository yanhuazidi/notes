#charset:utf-8

for x in [1,2,3,4,5]:
    for y in ['a','b','c','d',3]:
        if x==y:
            print(x)

print([y for x in [1,2,3,4,5] for y in ['a','b','c','d',3] if x==y])



