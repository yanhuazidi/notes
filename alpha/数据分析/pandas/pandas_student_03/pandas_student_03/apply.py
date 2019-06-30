import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(4, 5), columns=['A', 'B', 'C', 'D', 'E'])
print(df)
# 计算各列数据总和并作为新列添加到末尾
df['Col_sum']=df.apply(lambda x:x.sum(),axis=1)
# 计算各行数据总和并作为新行添加到末尾
df.loc['Row_sum']=df.apply(lambda x:x.sum(),axis=0)
print(df)
