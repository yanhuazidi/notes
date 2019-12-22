# -*- coding: utf-8 -*-
from __future__ import unicode_literals
'''
测试numpy标准差函数
'''
import numpy as np
# 读取收盘价
closing_prices = np.loadtxt(
    '../data/aapl.csv', delimiter=',',
    usecols=(6,), unpack=True)
print(closing_prices)
# 计算标准差
print(np.std(closing_prices))
# ddof为修正值  ddof=1时
# 求标准差时的分母将会是n-1
print(np.std(closing_prices, ddof=1))

# 手动计算标准差
mean = np.mean(closing_prices)  # 算数均值
devs = closing_prices - mean  # 离差数组
dsqs = devs ** 2  # 离差方数组
pvar = np.sum(dsqs) / dsqs.size  # 总体方差
pstd = np.sqrt(pvar)  # 总体标准差
print('pstd:', pstd)
# 样本方差
svar = np.sum(dsqs) / (dsqs.size - 1)
sstd = np.sqrt(svar)  # 样本标准差
print('sstd:', sstd)
