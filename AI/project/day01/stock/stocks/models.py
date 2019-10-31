from django.db import models

# Create your models here.
股票表Stock
id
stonumber 股票编码 C 20
company_name 公司名称 C 60
industry 细分行业 C 50
area 地区 C 50
pe 市盈率 De
outstanding 流通股本 De
totals 总股本 De
totalAssets 总资产 De
liquidAssets 流动资产 De
fixAssets 固定资产 De
reserved 公积金 De
reservedPerShare 每股公积金 De
esp 每股收益 De
bvps 每股净资 De
pb 市净率 De
timeToMarket 上市日期 Da
isDelete 是否删除 B

广告表Ad
id
title 广告名 C 50
callback_url 广告链接 url
adimg 广告图片 Image
isDelete 是否删除 B

新闻资讯News
id
title 标题 C
body 内容 Text
datetime 发布日期 Da
阅读量 I
isDelete 是否删除 B
