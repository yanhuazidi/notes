import pandas as pd
import numpy as np
#给定以下数据
df = pd.DataFrame({'A': [1, 1, 2, 2],
                   'B': [1, 2, 3, 4],
                   'C': np.random.randn(4)})
print(df)
# 按照A列分组后聚合求最小值 df1接收
df1=df.groupby('A').agg('min')
# print(df1)
# 按照A列分组后聚合求最小值和最大值 df2接收
df2=df.groupby('A').agg(['min','max'])
# print(df2)
# 按照A列分组后聚合后对B列求最小值和最大值，
# 对C列求和，df3接收
df3=df.groupby('A').agg({'B':['min','max'],'C':'sum'})
print(df3)