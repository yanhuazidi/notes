# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
# 读取训练数据
x, y = [], []
with open('../../data/abnormal.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
# 二维数组形式的输入矩阵，一行一样本，一列一特征
x = np.array(x)
# 一维数组形式的输出序列，每个元素对应一个输入样本
y = np.array(y)
# 创建线性回归器
model1 = lm.LinearRegression()
# 用已知的输入和输出训练线性回归器
model1.fit(x, y)
# 根据给定的输入预测对应的输出
pred_y1 = model1.predict(x)
# 创建岭回归器
model2 = lm.Ridge(150)
# 用已知的输入和输出训练岭回归器
model2.fit(x, y)
# 根据给定的输入预测对应的输出
pred_y2 = model2.predict(x)
# 可视化回归曲线
mp.figure('Linear & Ridge', facecolor='lightgray')
mp.title('Linear & Ridge', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75, s=60,
           label='Sample')
sorted_indices = x.T[0].argsort()
mp.plot(x[sorted_indices], pred_y1[sorted_indices],
        c='orangered', label='Linear')
mp.plot(x[sorted_indices], pred_y2[sorted_indices],
        c='limegreen', label='Ridge')
mp.legend()
mp.show()
