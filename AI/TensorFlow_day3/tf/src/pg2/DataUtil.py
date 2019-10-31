import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

# 加载数据
def loadData(filename):
    """

    :param filename:
    :return: mnist数据集
    mnist.train:55000
                images:以二进制格式存储图片,28*28共784个像素值
                labels:图片对应的标签,默认以十进制格式存储0~9
    mnist.validation:5000
                images:以二进制格式存储图片,28*28共784个像素值
                labels:图片对应的标签,默认以十进制格式存储0~9
     mnist.test:10000
                images:以二进制格式存储图片,28*28共784个像素值
                labels:图片对应的标签,默认以十进制格式存储0~9
    """
    mnist=input_data.read_data_sets(filename,one_hot=True)
    mnist.train.cls=np.argmax( mnist.train.labels,axis=1)
    mnist.test.cls = np.argmax(mnist.test.labels, axis=1)
    mnist.validation.cls = np.argmax(mnist.validation.labels, axis=1)
    return mnist

mnist=loadData('../../dataset/mnist')
print(mnist.train.images.shape)

def plotData(imgs,cls,pred=None):
    """
    数据可视化
    :param imgs: 可视化图片
    :param cls: 图片的真实标签
    :param pred: 图片的预测结果,默认为None
    :return: 无
    """
    assert len(imgs)==len(cls)==9
    fix,aixs=plt.subplots(3,3)
    for i,aix in enumerate(aixs.flat):
        # 修改图片维度为28*28,使用二级制格式读取
        aix.imshow(imgs[i].reshape((28,28)),cmap='binary')
        lbls=''
        if pred is None:
            lbls='true:{0}'.format(cls[i])
        else:
            lbls='true:{0};pred:{1}'.format(cls[i],pred[i])
        aix.set_xlabel(lbls) # x轴标题
        aix.set_xticks([]) # 刻度清零
        aix.set_yticks([])

    # 显示图片
    plt.show()

plotData(mnist.test.images[:9],mnist.test.cls[:9])
