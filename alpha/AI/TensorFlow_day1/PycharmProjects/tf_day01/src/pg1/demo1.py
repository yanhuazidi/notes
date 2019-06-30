"""
 1 导入库
"""
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


"""
 2 数据预处理: 加载数据   分割数据   数据可视化 
"""
x=[[0,0],[1,0],[0,1],[1,1],[1,1],[0,0]]
print(np.array(x))
y=[0,1,1,1,1,0]
for lbl,dt in zip(y,x):
    plt.plot(dt[0],dt[1],
             'o' if lbl else '^',    # 形状
             mec='r' if lbl else 'b' ) # 颜色
plt.show()






# 数据可视化,绘制训练样本的散点图
# 将标签为0的数据显示为绿色
# 将标签为1的数据显示为红色




"""
 3 构建神经网络
"""
# x:[6,2]
# weights: 2,1
# 参数1:均值
# 参数2:标准差
# 参数3:生成维度
weights=np.random.normal(0, 0.001,
                         size=[np.array(x).shape[1],1])
# 阈值有多种初始化方式,可以初始化为1或0.5,也可以随机生成
bias= np.random.normal(0, 0.001, size=1)
print(weights)
print(bias)

print(np.dot(x,weights)+bias)

"""
 4 训练模型
"""
# 激活函数
def f(lin_r):
    return 1 if lin_r>0 else 0

# 预测输出
def predict(vec,theta,b):
    '''
    :param vec: 输入的特征向量
    :param theta: 权重参数
    :param b: 阈值
    :return: 预测结果
    '''
    return f(np.dot(vec,theta)+b)

# 测试代码,输出训练集预测的结果
for v in x:
    print(predict(v,weights,bias))


"""
 5 优化
 反向传播算法:通过预测结果计算预测的误差,根据误差反向调整
                权重参数和阈值               
"""
def update_theta(pred,y_true,rate,vec):
    '''
    :param pred: 预测结果
    :param y_true: 正确标签
    :param rate: 学习速率,优化速度
    :param vec: 输入值
    :return:
    '''
    # 误差函数
    loss = y_true-pred

    # 调整权重参数
    global weights
    weights= list(map(lambda x1:x1[0]+x1[1]*loss*rate,
                   list(zip(weights,vec))))
    global bias
    bias =bias+ loss*rate

def one_iter():
    samples=zip(x,y) # 打包训练样本和标签
    for v,lbl in samples:
        pred=predict(v,weights,bias) # 预测结果
        update_theta(pred,lbl,0.1,v)# 调整权重

# 测试代码
for i in range(1000):
    one_iter()
print(weights)
print(bias)

input_x=[0,0]
output_y=predict(input_x,weights,bias)
print(output_y)

"""
  6 性能评估
"""

