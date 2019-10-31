# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [1, 3, 2],
    [7, 5, 4],
    [1, 8, 6],
    [7, 3, 9]])
# 构造编码字典列表
code_tables = []
for col in raw_samples.T:
    # 构造针对特定列的字典
    code_table = {}
    for val in col:
        code_table[val] = None
    # 将该列的编码字典加到编码字典列表中
    code_tables.append(code_table)
# 填写编码字典列表中每个编码字典的值
for code_table in code_tables:
    size = len(code_table)
    for one, key in enumerate(
            sorted(code_table.keys())):
        code_table[key] = np.zeros(
            shape=size, dtype=int)
        code_table[key][one] = 1
# 按照编码字典列表对原始样本矩阵做独热编码
ohe_samples = []
for raw_sample in raw_samples:
    ohe_sample = np.array([], dtype=int)
    for i, key in enumerate(raw_sample):
        ohe_sample = np.hstack((
            ohe_sample, code_tables[i][key]))
    ohe_samples.append(ohe_sample)
ohe_samples = np.array(ohe_samples)
print(ohe_samples)
# 创建独热编码器
ohe = sp.OneHotEncoder(sparse=False, dtype=int)
# 用独特编码器对原始样本矩阵做独热编码
ohe_samples = ohe.fit_transform(raw_samples)
print(ohe_samples)
