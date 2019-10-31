# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
# 读取训练数据
train_x, train_y = [], []
with open('../../data/single.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        train_x.append(data[:-1])
        train_y.append(data[-1])
# 二维数组形式的输入矩阵，一行一样本，一列一特征
train_x = np.array(train_x)
# 一维数组形式的输出序列，每个元素对应一个输入样本
train_y = np.array(train_y)
# 将一个多项式特征扩展预处理器和
# 一个线性回归器串联为一个管线
model = pl.make_pipeline(sp.PolynomialFeatures(10),
                         lm.LinearRegression())
# 用已知的输入和输出训练线性回归器
model.fit(train_x, train_y)
# 根据给定的输入预测对应的输出
pred_train_y = model.predict(train_x)
# R2得分[0,1]
print(sm.r2_score(train_y, pred_train_y))
# 在训练集之外构造测试集
test_x = np.linspace(
    train_x.min(), train_x.max(), 1000)[:, np.newaxis]
pred_test_y = model.predict(test_x)
# 可视化回归曲线
mp.figure('Polynomial Regression', facecolor='lightgray')
mp.title('Polynomial Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, c='dodgerblue',
           alpha=0.75, s=60, label='Sample')
mp.plot(test_x, pred_test_y, c='orangered',
        label='Regression')
mp.legend()
mp.show()
