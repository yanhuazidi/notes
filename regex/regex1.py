
import re

pattern=r"abcd(?P<Dog>ef)"

regex = re.compile(pattern)

obj = regex.search("abcdefgh")

print(regex.pattern)
print(regex.groups)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)
print("-------------------")
print(obj.span())
print(obj.group('Dog'))
print(obj.groupdict())
print(obj.groups())