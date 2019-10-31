import pandas as pd
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
#读取电影详情表 movies
movies=pd.read_table('movies.dat',sep='::'
                     ,header=None
                     ,names=['MovieID','Title','Genres']
                     ,engine='python')
# print(movies.head())
#读取评分表 Ratings
Ratings=pd.read_table('ratings.dat',header=None
                      ,names=['UserID','MovieID','Rating','Timestamp']
                      ,engine='python',sep='::')
# print(Ratings.head())
# print(len(Ratings))
# 读取test.csv表格
csv=pd.read_csv('test.csv',engine='python')
# print(csv.head())
# print(len(csv))
# 描述性统计分析
# print(csv.describe())
print(csv.info())
# PassengerId => 乘客ID
# Pclass => 乘客等级(1/2/3等舱位)
# Name => 乘客姓名
# Sex => 性别
# Age => 年龄
# SibSp => 堂兄弟/妹个数
# Parch => 父母与小孩个数
# Ticket => 船票信息
# Fare => 票价
# Cabin => 客舱
# Embarked => 登船港口

