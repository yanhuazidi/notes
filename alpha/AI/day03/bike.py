# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import csv
import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp
with open('../../data/bike_day.csv') as f:
    reader = csv.reader(f)
    x, y = [], []
    for row in reader:
        x.append(row[2:13])
        y.append(row[-1])
fn_day = np.array(x[0])
x = np.array(x[1:], float)
y = np.array(y[1:], float)
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]
# 由1000棵最大树高为10的决策树组成的随机森林
# 回归器，其中每棵决策树的最小可划分样本数为2
model = se.RandomForestRegressor(
    max_depth=10, n_estimators=1000,
    min_samples_split=2)
model.fit(train_x, train_y)
fi_day = model.feature_importances_
with open('../../data/bike_hour.csv') as f:
    reader = csv.reader(f)
    x, y = [], []
    for row in reader:
        x.append(row[2:14])
        y.append(row[-1])
fn_hour = np.array(x[0])
x = np.array(x[1:], float)
y = np.array(y[1:], float)
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]
# 由1000棵最大树高为10的决策树组成的随机森林
# 回归器，其中每棵决策树的最小可划分样本数为2
model = se.RandomForestRegressor(
    max_depth=10, n_estimators=1000,
    min_samples_split=2)
model.fit(train_x, train_y)
fi_hour = model.feature_importances_
# 可视化特征重要性排序
mp.figure('Bike', facecolor='lightgray')
mp.subplot(211)
mp.title('Day', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_day.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fi_day[sorted_indices],
       facecolor='deepskyblue', edgecolor='steelblue')
mp.xticks(pos, fn_day[sorted_indices], rotation=30)
mp.subplot(212)
mp.title('Hour', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_hour.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fi_hour[sorted_indices],
       facecolor='lightcoral', edgecolor='indianred')
mp.xticks(pos, fn_hour[sorted_indices], rotation=30)
mp.tight_layout()
mp.show()
