import numpy as np
import tensorflow as tf
from src.pg2.DataUtil import *
import os
import time
from datetime import timedelta


# 输入层
x=tf.placeholder(tf.float32,shape=[None,784])
y=tf.placeholder(tf.float32,shape=[None,10])
# 将输入数据修改为矩阵
# shape:[样本数量,行,列,颜色通道]
x_imgs=tf.reshape(x,shape=[-1,28,28,1])
# 样本真实标签
y_true=tf.argmax(y,dimension=1)


# 卷积层1,32个结果,28*28
conv1=tf.layers.conv2d(inputs=x_imgs,   # 输入数据
                       filters=32,       # 卷积核的数量
                       kernel_size=[5,5], # 卷积核大小
                       padding='same',          # 是否需要填充
                       activation=tf.nn.relu)   # 卷积运算之后使用的激活函数


# 池化层1,32个,14*14
pool1=tf.layers.max_pooling2d(inputs=conv1,pool_size=[2,2],strides=2)


# 卷积层2,64个14*14
conv2=tf.layers.conv2d(inputs=pool1,   # 输入数据
                       filters=64,       # 卷积核的数量
                       kernel_size=[5,5], # 卷积核大小
                       padding='same',          # 是否需要填充
                       activation=tf.nn.relu)   # 卷积运算之后使用的激活函数


# 池化层2,64个,7*7
pool2=tf.layers.max_pooling2d(inputs=conv2,pool_size=[2,2],strides=2)


# 对池化结果进行扁平化操作
flat=tf.reshape(pool2,shape=[-1,7*7*64])

# 全连接层1
full1=tf.layers.dense(inputs=flat,units=1024,activation=tf.nn.relu)

# 防止过拟合
dp=tf.layers.dropout(inputs=full1,rate=0.4)


# 全连接层2
"""
  最后的输出层,输出是0~9这10个数字的概率值,输入多分类的情况,
  不再使用relu激活函数,使用softmax激活函数
  对于二分类情况,则使用sigmoid激活函数
  
"""
full2 =tf.layers.dense(inputs=dp,units=10)
logit =tf.nn.softmax(full2)# 归一化
pred=tf.argmax(logit,dimension=1)# 预测类别

# 利用交叉熵定义损失函数
cross=tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=logit)
cost=tf.reduce_mean(cross) # 损失均值

# 优化
train=tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)

# 性能评估
corr_pred=tf.equal(y_true,pred)
acc=tf.reduce_mean(tf.cast(corr_pred,tf.float32))


# 保存训练模型
# 创建保存路径
save_dir='checkpoint/'
if not os.path.exists(save_dir): # 如果路径不存在
    os.makedirs(save_dir)
save_path=os.path.join(save_dir,'besetmodel')

# 模型保存对象
saver=tf.train.Saver()


# 分批次训练样本的数量
batch_size=64

def opt(num_iter):
    """
    训练过程
    :param num_iter: 迭代更新的次数
    :return: 无
    """
    session=tf.Session()
    session.run(tf.global_variables_initializer())

    # 最优准确率
    best_acc=0

    for i in range(1,num_iter+1):
        # 产生参与训练的样本
        x_batch,y_batch=mnist.train.next_batch(batch_size)
        # 执行优化与性能评估
        _,ac=session.run([train,acc],feed_dict={x:x_batch,y:y_batch})

        if i%100==0:
            print('迭代次数:{0},准确率:{1}'.format(i,ac))

        if ac>best_acc:
            best_acc=ac
            # 保存模型文件
            saver.save(sess=session,save_path=save_path)

    # 使用训练后的权重参数,输出测试集第一个样本的标签
    pred_test=session.run(pred,feed_dict={x:mnist.test.images[:1]})
    print(pred_test)
    print('正确标签:{0}'.format(mnist.test.cls[:1]))

# 运行
opt(num_iter=5000)

























# session=tf.Session() # 创建会话
# session.run(tf.global_variables_initializer()) # 初始化全局变量
# result,pd,loss=session.run([logit,pred,cost],feed_dict={x:mnist.train.images[:2],y:mnist.train.labels[:2]})
#
# print(result)
# print(pd)
# print(loss)



# # 执行卷积层2,池化层2,传入两个训练样本,获取执行的结果
# c2,p2=session.run([conv2,pool2],feed_dict={x:mnist.train.images[:2]})
# print('conv2')
# print(c2)
# print('pool2')
# print(p2)
# print(c2.shape)
# print(p2.shape)






