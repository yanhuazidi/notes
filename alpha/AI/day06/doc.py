# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb
# 训练数据集
train = sd.load_files(
    '../../data/20news', encoding='latin1',
    shuffle=True, random_state=7)
train_data = train.data
train_y = train.target
categories = train.target_names
# 计数矢量化器
cv = ft.CountVectorizer()
# 词袋矩阵
train_bow = cv.fit_transform(train_data)
# 词频逆文档频率转换器
tt = ft.TfidfTransformer()
# 词频逆文档频率矩阵
train_x = tt.fit_transform(train_bow)
# 基于多项分布的朴素贝叶斯分类器
model = nb.MultinomialNB()
# 训练分类器
model.fit(train_x, train_y)
# 测试数据集
test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar eipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads']
# 词袋矩阵
test_bow = cv.transform(test_data)
# 词频逆文档频率矩阵
test_x = tt.transform(test_bow)
# 预测测试数据集的类别
pred_test_y = model.predict(test_x)
# 打印预测的结果
for sentence, index in zip(test_data, pred_test_y):
    print(sentence, '->', categories[index])
