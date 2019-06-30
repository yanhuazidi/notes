# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试numpy自定义复合类型
在ndarray数组中存储3位学生信息
'''
import numpy as np

data = [('zs', [10, 15, 2], 3),
        ('ls', [12, 12, 92], 8),
        ('ww', [14, 35, 82], 13)]

# 第一种设置dtype的方式
a = np.array(data,
             dtype='U2, 3i4, i4')
print(a, '; zs.age:', a[0]['f2'])

# 第二种设置dtype的方式
b = np.array(data, dtype=[
    ('name', 'str_', 2),
    ('scores', 'int32', 3),
    ('age', 'int32', 1)])
print(b, '; ww.age:', b[2]['age'])

# 第三种设置dtype的方式
c = np.array(data, dtype={
    'names': ['name', 'scores', 'age'],
    'formats': ['U2', '3int32', 'int32']})
print(c, '; ls.name:', c[1]['name'])

# 第四种设置dtype的方式
# 例如scores字段在存储时将会从第16个字节
# 开始输出分数列表数据,3int32将会占用12
# 字节,那么age字段将会从第28个字节开始
# 向后输出.
# U2占用了8字节, 与scores字段中间将会
# 空出8个字节.虽然浪费了空间,但是这种数据
# 存储对齐的做法在数据访问时将提高效率.
d = np.array(data, dtype={
    'name': ('U2', 0),
    'scores': ('3int32', 16),
    'age': ('int32', 28)})

# 第五种设置dtype的方式
e = np.array([0x123456, 0x56789a],
             dtype=('u4',
                    {'lowc': ('u1', 0),
                     'midc': ('u1', 1),
                     'high1c': ('u1', 2),
                     'high2c': ('u1', 3)}))
print('%x' % e[0])  # 1234
print('%x' % e['lowc'][0])   # 34
print('%x' % e['high1c'][0])  # 12

# ndarray对象处理日期类型元素
f = np.array(['2018', '2019-01-01',
              '2019-02-01',
              '2019-01-02 01:01:01'])
# 把f数组的元素类型改为日期类型
g = f.astype('M8[D]')
print(g, '; g.dtype:', g.dtype)

h = g.astype('int32')
print(h)
print(h[2] - h[1])
