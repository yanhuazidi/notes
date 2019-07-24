

[TOC]



### 列表推导式嵌套

```python
for x in [1,2,3,4,5]:
    for y in ['a','b','c','d',3]:
        if x==y:
            print(x)

print([y for x in [1,2,3,4,5] for y in ['a','b','c','d',3] if x==y])

```



### 把推导式作实参

```python
version = '.'.join(str(s) for s in version_info[:2])
```









### 赋值的打包与解包

```python
RELEASE_LEVELS = [ALPHA, BETA, RELEASE_CANDIDATE, FINAL] = ['alpha', 'beta', 'candidate', 'final']
RELEASE_LEVELS_DISPLAY = {ALPHA: ALPHA,
                          BETA: BETA,
                          RELEASE_CANDIDATE: 'rc',
                          FINAL: ''}
```

