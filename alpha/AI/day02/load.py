# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pickle
import numpy as np
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
# 读取训练数据
x, y = [], []
with open('../../data/single.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
# 二维数组形式的输入矩阵，一行一样本，一列一特征
x = np.array(x)
# 一维数组形式的输出序列，每个元素对应一个输入样本
y = np.array(y)
# 加载模型
with open('../../data/linear.pkl', 'rb') as f:
    model = pickle.load(f)
# 根据给定的输入预测对应的输出
pred_y = model.predict(x)
# 评估指标
print(sm.mean_absolute_error(y, pred_y))  # 平均绝对值误差
print(sm.mean_squared_error(y, pred_y))  # 平均平方误差
print(sm.median_absolute_error(y, pred_y))  # 中位绝对值误差
print(sm.r2_score(y, pred_y))  # R2得分[0,1]
# 可视化回归曲线
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75, s=60,
           label='Sample')
sorted_indices = x.T[0].argsort()
mp.plot(x[sorted_indices], pred_y[sorted_indices],
        c='orangered', label='Regression')
mp.legend()
mp.show()
