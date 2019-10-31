# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb
import sklearn.metrics as sm
import matplotlib.pyplot as mp
x, y = [], []
with open('../../data/multiple1.txt', 'r') as f:
    for line in f.readlines():
        data = [float(substr) for substr
                in line.split(',')]
        x.append(data[:-1])
        y.append(data[-1])
x = np.array(x)
y = np.array(y, dtype=int)
# 划分训练集和测试集
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25,
                        random_state=7)
# 创建高斯分布朴素贝叶斯分类器
model = nb.GaussianNB()
# 交叉验证
pws = ms.cross_val_score(
    model, train_x, train_y, cv=5,
    scoring='precision_weighted')
print(pws.mean())
rws = ms.cross_val_score(
    model, train_x, train_y, cv=5,
    scoring='recall_weighted')
print(rws.mean())
f1s = ms.cross_val_score(
    model, train_x, train_y, cv=5,
    scoring='f1_weighted')
print(f1s.mean())
model.fit(train_x, train_y)  # 用训练集训练模型
l, r, h = x[:, 0].min() - 1, x[:, 0].max() + 1, 0.005
b, t, v = x[:, 1].min() - 1, x[:, 1].max() + 1, 0.005
grid_x = np.meshgrid(np.arange(l, r, h),
                     np.arange(b, t, v))
flat_x = np.c_[grid_x[0].ravel(), grid_x[1].ravel()]
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
# 用测试集评估模型的性能
pred_test_y = model.predict(test_x)
# 计算并打印模型预测的混淆矩阵
cm = sm.confusion_matrix(test_y, pred_test_y)
print(cm)
cr = sm.classification_report(test_y, pred_test_y)
print(cr)
mp.figure('Naive Bayes Classification', facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y,
           cmap='brg', s=80)
mp.show()
