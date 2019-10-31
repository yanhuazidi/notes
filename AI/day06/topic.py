# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import warnings
warnings.filterwarnings(
    'ignore', category=UserWarning)
import nltk.tokenize as tk
import nltk.corpus as nc
import nltk.stem.snowball as sb
import gensim.models.ldamodel as gm
import gensim.corpora as gc
doc = []
with open('../../data/topic.txt', 'r') as f:
    for line in f.readlines():
        doc.append(line[:-1])
tokenizer = tk.RegexpTokenizer(r'\w+')
stopwords = nc.stopwords.words('english')
stemmer = sb.SnowballStemmer('english')
lines_tokens = []
for line in doc:
    tokens = tokenizer.tokenize(line.lower())
    line_tokens = []
    for token in tokens:
        if token not in stopwords:
            token = stemmer.stem(token)
            line_tokens.append(token)
    lines_tokens.append(line_tokens)
dic = gc.Dictionary(lines_tokens)
bow = []
for line_tokens in lines_tokens:
    row = dic.doc2bow(line_tokens)
    bow.append(row)
model = gm.LdaModel(
    bow, num_topics=2, id2word=dic, passes=25)
topics = model.print_topics(num_topics=2, num_words=4)
print(topics)
