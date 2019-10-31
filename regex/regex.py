import re

pattern=r"\d+"

s = "2008年事情多,08奥运,512地震"

# l = re.findall(pattern,s)
# print(l)

regex = re.compile(pattern)
l = regex.findall(s)

# l = re.split(r'\s+',"Hello world")
# s = re.subn(r"\s+","##","hello world")

it = re.finditer(pattern,s)
print(it)
for i in it:
    print(i)
    print(i.group())