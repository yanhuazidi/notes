#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/29 下午6:07 
# @Author : yrh
# @Site :  
# @File : demo1.py 
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import time
from datetime import timedelta
import os
import src.inception as inception
import src.cifar10 as cifar10
from src.cifar10 import num_classes
import prettytensor as pt

inception.maybe_download()
model=inception.Inception()

def classify(image_path):
    pred=model.classify(image_path=image_path)
    model.print_scores(pred=pred,k=10,only_first_name=True)
def plot_resize_image(image_path):
    resize_image=model.get_resized_image(image_path=image_path)
    plt.imshow(resize_image,interpolation='nearest')
    plt.show()
img_path=os.path.join('../images/parrot.jpg')
plot_resize_image(img_path)
images_train,cls_train,lables_train=cifar10.load_training_data()
def plot_scatter(values, cls):
    # Create a color-map with a different color for each class.
    import matplotlib.cm as cm
    cmap = cm.rainbow(np.linspace(0.0, 1.0, num_classes))

    # Get the color for each sample.
    colors = cmap[cls]

    # Extract the x- and y-values.
    x = values[:, 0]
    y = values[:, 1]

    # Plot it.
    plt.scatter(x, y, color=colors)
    plt.show()
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
print(images_train.shape)
reduced=images_train[0:3000]
cls=cls_train[0:3000]
plot_scatter(reduced,cls)









# # 数据预处理
# # images_train,cls_train,labels_train=cifar10.load_training_data()
# # print(images_train.shape)