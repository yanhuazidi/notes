# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
doc = 'The brown dog is running. ' \
    'The black dog is in the black room. ' \
    'Running in the room is forbidden.'
print(doc)
sentences = tk.sent_tokenize(doc)
print(sentences)
# 计数矢量化器
cv = ft.CountVectorizer()
bow = cv.fit_transform(sentences).toarray()  # 词袋矩阵
print(bow)
dict = cv.get_feature_names()  # 词典列表
print(dict)
