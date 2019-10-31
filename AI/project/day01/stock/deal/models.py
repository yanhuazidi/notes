from django.db import models

# Create your models here.
自选股表SelfStock
id
user 用户（F UserInfo）
stock 股票（F Stock）

挂单表BOSStock
id
user 用户（F UserInfo）
stock 股票（F Stock）
role 角色（买/卖）Ic
price 价格 De
amount 数量 I
datetime 时间 Da

交易记录表DealStock
id
buser 买家（F UserInfo）
suser 卖家（F UserInfo）
price 价格 De
amount 数量 I
stock 股票（F Stock）
datetime 时间 Da
