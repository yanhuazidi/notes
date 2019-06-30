import numpy as np
import pandas as pd
# 核心代码，设置显示的最大列、宽等参数，
# 消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
# 获取电影数据表格
users = pd.read_table('users.dat',header=None,names=['UserID','Gender','Age','Occupation','Zip-code'], sep='::',engine= 'python')
print(users.head())
#获取csv文件,定义列名为width,height,category

#获取表格文件



