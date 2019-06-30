import re

# s = 'Hello World'
# pattern=r'hello'
# regex = re.compile(pattern,flags=re.I)

s = '''Hello World
hello kitty
你好
'''
pattern=r'''Hello   #匹配hello
\s+     #匹配空字符
World   #匹配world
'''
regex = re.compile(pattern,flags=re.X)
try:
    s = regex.search(s).group()
except Exception:
    print("没有匹配到内容")
else:
    print(s)