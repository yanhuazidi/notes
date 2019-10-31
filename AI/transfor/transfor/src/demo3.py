#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/31 下午11:07 
# @Author : yrh
# @Site :  
# @File : demo3.py 
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import os
import src.inception as inception
import src.cifar10 as cifar10
import time
from datetime import timedelta
from src.cifar10 import num_classes
from sklearn.decomposition import PCA
import matplotlib.cm as  cm
# 加载数据
cifar10.maybe_download_and_extract()
class_names=cifar10.load_class_names()
print(class_names)
# 加载训练数据和测试数据
images_train,cls_train,labels_train=cifar10.load_training_data()
images_test,cls_test,labels_test=cifar10.load_test_data()

# 数据可视化
def plot_images(images, cls_true, cls_pred=None, smooth=True):
    assert len(images) == len(cls_true)

    # 划分子窗口
    fig, axes = plt.subplots(3, 3)

    # 子窗口间隔
    if cls_pred is None:
        hspace = 0.3
    else:
        hspace = 0.6
    fig.subplots_adjust(hspace=hspace, wspace=0.3)

    # 填充方式
    if smooth:
        interpolation = 'spline16'
    else:
        interpolation = 'nearest'

    for i, ax in enumerate(axes.flat):
        if i < len(images):
            # 显示图片
            ax.imshow(images[i],
                      interpolation=interpolation)

            # 图片标签
            cls_true_name = class_names[cls_true[i]]

            # 显示图片和图片标签
            if cls_pred is None:
                xlabel = "True: {0}".format(cls_true_name)
            else:
                # 预测结果
                cls_pred_name = class_names[cls_pred[i]]

                xlabel = "True: {0}\nPred: {1}".format(cls_true_name, cls_pred_name)

            # 显示x轴标题
            ax.set_xlabel(xlabel)

        # 清楚刻度
        ax.set_xticks([])
        ax.set_yticks([])
    plt.show()

# 图片
images = images_test[0:9]

# 标签
cls_true = cls_test[0:9]
plot_images(images=images, cls_true=cls_true, smooth=False)

inception.maybe_download()
model=inception.Inception()
from src.inception import transfer_values_cache
file_path_cache_train = os.path.join(cifar10.data_path, 'inception_cifar10_train.pkl')
file_path_cache_test = os.path.join(cifar10.data_path, 'inception_cifar10_test.pkl')
# inception的图片颜色值是0~255之间，cifar10的图片颜色值是01之间，需要调整颜色
images_scaled=images_train*255.0
print(images_train[0])
print(images_scaled[0])
# 在训练集中有50,000张图像，每张图像有2048个transfer-values
transfer_values_train=transfer_values_cache(cache_path=file_path_cache_train,model=model,images=images_scaled)
images_scaled=images_test*255.0
transfer_values_test=transfer_values_cache(cache_path=file_path_cache_test,model=model,images=images_scaled)

def plot_transfer_values(i):
    print('input imafe')
    plt.imshow(images_train[i],interpolation='nearest')
    plt.show()
    img=transfer_values_test[i]
    img=img.reshape((32,64))
    plt.imshow(img,interpolation='nearest',cmap='Reds')
    plt.show()

# 使用pca降维
pca=PCA(n_components=2)
transfer_values=transfer_values_train[:3000]
cls=cls_train[:3000]
# 调用pca函数将transfer_values从2048维降为2维
transfer_values_reduced=pca.fit_transform(transfer_values)
# 绘制降维后样本分布散点图
def plot_scotter(values,cls):
    cmap=cm.rainbow(np.linspace(0.0, 1.0, num_classes))
    colors=cmap[cls]
    x=values[:0]
    y=values[:1]
    plt.scatter(x,y,c=colors)
    plt.show()




