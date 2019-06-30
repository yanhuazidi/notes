# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms
import matplotlib.pyplot as mp
data = []
with open('../../data/car.txt', 'r') as f:
    for line in f.readlines():
        data.append(line[:-1].split(','))
data = np.array(data).T
encoders, train_x = [], []
for row in range(len(data)):
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        train_x.append(encoder.fit_transform(data[row]))
    else:
        train_y = encoder.fit_transform(data[row])
    encoders.append(encoder)
train_x = np.array(train_x).T
model = se.RandomForestClassifier(
    max_depth=8, random_state=7)
n_estimators = np.arange(50, 550, 50)
_, test_scores = ms.validation_curve(
    model, train_x, train_y, 'n_estimators',
    n_estimators, cv=5)
test_means1 = test_scores.mean(axis=1)
model = se.RandomForestClassifier(
    n_estimators=200, random_state=7)
max_depth = np.arange(1, 11)
_, test_scores = ms.validation_curve(
    model, train_x, train_y, 'max_depth',
    max_depth, cv=5)
test_means2 = test_scores.mean(axis=1)
mp.figure('n_estimators', facecolor='lightgray')
mp.title('n_estimators', fontsize=20)
mp.xlabel('n_estimators', fontsize=14)
mp.ylabel('F1 Score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(n_estimators, test_means1, 'o-',
        c='dodgerblue', label='Testing')
mp.legend()
mp.figure('max_depth', facecolor='lightgray')
mp.title('max_depth', fontsize=20)
mp.xlabel('max_depth', fontsize=14)
mp.ylabel('F1 Score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(max_depth, test_means2, 'o-',
        c='orangered', label='Testing')
mp.legend()
mp.show()
