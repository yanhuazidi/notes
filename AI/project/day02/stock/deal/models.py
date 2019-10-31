from django.db import models
from userinfo.models import *
from stocks.models import *
# Create your models here.

ROLE_CHOICES ={
    (0,'买'),
    (1,'卖'),
}


class SelfStock(models.Model):
    user = models.ForeignKey(UserInfo)
    stock = models.ForeignKey(Stock)

    def __str__(self):
        return self.user.username




class BOSStock(models.Model):
    user = models.ForeignKey(UserInfo)
    stock = models.ForeignKey(Stock)
    role = models.IntegerField(verbose_name='角色', choices=ROLE_CHOICES, default=0)
    price = models.DecimalField(verbose_name='价格', max_digits=8, decimal_places=2)
    amount = models.IntegerField(verbose_name='数量')
    datetime = models.DateTimeField(verbose_name='时间',auto_now_add=True)

    def __str__(self):
        return self.user.username


class DealStock(models.Model):
    buser = models.ForeignKey(UserInfo, related_name='buser')
    suser = models.ForeignKey(UserInfo, related_name='suser')
    price = models.DecimalField(verbose_name='价格', max_digits=8, decimal_places=2)
    amount = models.IntegerField(verbose_name='数量')
    stock = models.ForeignKey(Stock)
    datetime = models.DateTimeField(verbose_name='时间', auto_now_add=True)

    def __str__(self):
        return self.stock.stonumber