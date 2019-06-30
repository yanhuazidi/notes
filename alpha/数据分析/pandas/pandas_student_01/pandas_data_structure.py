import pandas as pd
import numpy as np
# 创建一组Series数据
# 1.创建Series
s1=pd.Series([90,86,70],
             index=['leo','kate','john'])
# dict={'leo':90,'kate':86,'john':70}
# s1=pd.Series(dict)
# print(s1)
# 通过绝对位置查找
# print(s1[0])
# 通过标签
# print(s1['leo'])
# 通过列表
# print(s1[['leo','kate']])
# 通过表达式
# print(s1[s1>80])
# 2.numpy中的ndarray：
s2=pd.Series(np.random.randn(5)
             ,index=list('ABCDE'))
# print(s2)
# 3.数字创建
s3=pd.Series(6)
# print(s3)
# 4.创建一组DataFrame数据-date_range创建时间
date=pd.date_range('20100101',periods=6)
# print(date)
df=pd.DataFrame(np.random.randn(6,4),index=date,
                columns=list('abcd'))
print(df)
# print(df.values)
# print(df.shape)
# a列数据
# print(df.a)
# print(df['a'])
# 访问a,b列数据
# print(df[['a','b']])
# 查看某几行
# print(df[0:4])
# print(df.head())

# loc查找
# print(df.loc['2010-01-01':'2010-01-04',['a','b']])
# iloc查找
# print(df.iloc[:4,[0,1]])
# ix查找
# print(df.ix[:4,['a','b']])
# loc表达式，得到2010-01-04之前的数据
print(df.loc[df.index<'20100104',['a','b']])
