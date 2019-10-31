# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
# 训练集输入数据
train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
# 训练集输出数据
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
# 迭代次数
n_epoches = 1000
# 学习率
lrate = 0.01
# 第几次迭代和每次迭代的损失值
epoches, losses = [], []
# 每次迭代的模型参数，初始模型：y = x + 1
w0, w1 = [1], [1]
# 迭代循环，epoch从1迭代到1000
for epoch in range(1, n_epoches + 1):
    # 记录这是第几次迭代
    epoches.append(epoch)
    # 根据预测函数y=w0+w1x，记录此次迭代的损失值
    losses.append(((train_y - (
        w0[-1] + w1[-1] * train_x)) ** 2
    ).sum() / 2)
    # 打印输出
    print('{:4}> w0={:.8f}, w1={:.8f}, loss={:.8f}'.format(
        epoches[-1], w0[-1], w1[-1], losses[-1]))
    # 损失函数关于w0的偏导数
    d0 = -(train_y - (
        w0[-1] + w1[-1] * train_x)).sum()
    # 损失函数关于w1的偏导数
    d1 = -((train_y - (
        w0[-1] + w1[-1] * train_x)) * train_x).sum()
    # 产生下一次迭代的w0
    w0.append(w0[-1] - lrate * d0)
    # 产生下一次迭代的w1
    w1.append(w1[-1] - lrate * d1)
# 将列表转换为数组，同时舍弃多余的模型参数
w0 = np.array(w0[:-1])
w1 = np.array(w1[:-1])
# 用训练集作为测试集计算实际的预测输出
sorted_indices = train_x.argsort()
test_x = train_x[sorted_indices]
test_y = train_y[sorted_indices]
pred_test_y = w0[-1] + w1[-1] * test_x
for y, pred_y in zip(test_y, pred_test_y):
    print(y, '->', pred_y)
# 计算损失函数曲面loss=f(w0,w1)上的点
grid_w0, grid_w1 = np.meshgrid(
    np.linspace(0, 9, 500),
    np.linspace(0, 3.5, 500))
flat_w0, flat_w1 = grid_w0.ravel(), grid_w1.ravel()
flat_loss = ((flat_w0 + np.outer(
    train_x, flat_w1) -
    train_y.reshape(-1, 1)) ** 2).sum(axis=0) / 2
grid_loss = flat_loss.reshape(grid_w0.shape)
# 可视化回归曲线
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, marker='s', c='dodgerblue',
           alpha=0.5, s=80, label='Training')
mp.scatter(test_x, test_y, marker='D', c='orangered',
           alpha=0.5, s=60, label='Testing')
mp.scatter(test_x, pred_test_y, c='orangered',
           alpha=0.5, s=80, label='Predicted')
for x, y, pred_y in zip(test_x, test_y, pred_test_y):
    mp.plot([x, x], [y, pred_y], c='orangered',
            alpha=0.5, linewidth=1)
mp.plot(test_x, pred_test_y, '--', c='limegreen',
        label='Regression', linewidth=1)
mp.legend()
# 可视化训练过程
mp.figure('Training Progress', facecolor='lightgray')
mp.subplot(311)
mp.title('Training Progress', fontsize=20)
mp.ylabel('w0', fontsize=14)
mp.gca().xaxis.set_major_locator(
    mp.MultipleLocator(100))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, w0, c='dodgerblue', label='w0')
mp.legend()
mp.subplot(312)
mp.ylabel('w1', fontsize=14)
mp.gca().xaxis.set_major_locator(
    mp.MultipleLocator(100))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, w1, c='limegreen', label='w1')
mp.legend()
mp.subplot(313)
mp.xlabel('epoch', fontsize=14)
mp.ylabel('loss', fontsize=14)
mp.gca().xaxis.set_major_locator(
    mp.MultipleLocator(100))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, losses, c='orangered', label='loss')
mp.legend()
mp.tight_layout()
# 可视化损失函数曲面
mp.figure('Loss Function')
ax = mp.gca(projection='3d')
mp.title('Loss Function', fontsize=20)
ax.set_xlabel('w0', fontsize=14)
ax.set_ylabel('w1', fontsize=14)
ax.set_zlabel('loss', fontsize=14)
mp.tick_params(labelsize=10)
ax.plot_surface(grid_w0, grid_w1, grid_loss,
                rstride=10, cstride=10, cmap='jet')
ax.plot(w0, w1, losses, 'o-', c='orangered',
        label='BGD')
mp.legend(loc='lower left')
mp.show()
