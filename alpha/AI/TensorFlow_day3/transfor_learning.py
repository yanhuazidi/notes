"""
    1 导入库
"""
import tensorflow as tf
import matplotlib.pyplot as plt
import os
import time
from datetime import timedelta
import src.inception as inception
import src.cifar10 as cifar10
from src.cifar10 import  num_classes


# 加载inception模型
inception.maybe_download()
# 定义inception模型对象
model=inception.Inception()

# 对图像进行识别
pred=model.classify(image_path='../images/parrot.jpg')
model.print_scores(pred=pred,k=10,only_first_name=True)


# 数据预处理
# 加载cifar10样本集相关参数
cifar10.maybe_download_and_extract()
class_names=cifar10.load_class_names()
# 下载训练集和测试集
images_train,cls_train,labels_train=cifar10.load_training_data()
images_test,cls_test,labels_test=cifar10.load_test_data()

# 数据可视化
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
        #
        aix.imshow(imgs[i])
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

plotData(images_train[:9],cls_train[:9])

# 训练样本测试样本的数据缓存
file_path_train_cache=os.path.join(cifar10.data_path,'file_path_train_cache')
file_path_test_cache=os.path.join(cifar10.data_path,'file_path_test_cache')

# 导入缓存模块
from src.inception import transfer_values_cache
images_sc=images_train*255 # 调整颜色范围
# 基于指定模型和新的数据进行数据缓存
transfer_values_train=transfer_values_cache(cache_path=file_path_train_cache,model=model,images=images_sc)


images_sc2=images_test*255 # 调整颜色范围
# 基于指定模型和新的数据进行数据缓存
transfer_values_test=transfer_values_cache(cache_path=file_path_test_cache,model=model,images=images_sc2)






