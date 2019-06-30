# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import sklearn.cluster as sc
import sklearn.neighbors as nb
import matplotlib.pyplot as mp
n_samples = 500
t = 2.5 * np.pi * (1 + 2 * np.random.rand(n_samples, 1))
x = 0.05 * t * np.cos(t)
y = 0.05 * t * np.sin(t)
n = 0.05 * np.random.rand(n_samples, 2)
x = np.hstack((x, y)) + n
# 无连续性凝聚层次聚类器
model = sc.AgglomerativeClustering(
    n_clusters=3, linkage='average')
model.fit(x)
pred_y1 = model.labels_  # 聚类标签
# 为每个样本建立一个包含10个最近邻的集合
conn = nb.kneighbors_graph(x, 10, include_self=False)
# 有连续性凝聚层次聚类器
# 在凝聚的过程中优先选择近邻中连续性最好的样本优先凝聚
model = sc.AgglomerativeClustering(
    n_clusters=3, linkage='average',
    connectivity=conn)
model.fit(x)
pred_y2 = model.labels_  # 聚类标签
# 可视化聚类
mp.figure('Nonconnectivity Agglomerative', facecolor='lightgray')
mp.title('Nonconnectivity Agglomerative', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.axis('equal')
mp.scatter(x[:, 0], x[:, 1], c=pred_y1, cmap='brg',
           s=80, alpha=0.5)
mp.figure('Connectivity Agglomerative', facecolor='lightgray')
mp.title('Connectivity Agglomerative', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.axis('equal')
mp.scatter(x[:, 0], x[:, 1], c=pred_y2, cmap='brg',
           s=80, alpha=0.5)
mp.show()
