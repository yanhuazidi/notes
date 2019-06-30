from django.db import models
from django.contrib.auth.models import AbstractUser

BANK_CHOICES = {
    (0,'中国银行'),
    (1,'招商银行'),
    (2,'中国建设银行'),
    (3,'中国交通银行'),
    (4,'我的银行'),
}

# Create your models here.
class UserInfo(AbstractUser):
    uphone = models.CharField('手机号', max_length=11,null=False)
    email = models.EmailField(verbose_name='邮箱')
    identity = models.CharField('身份证号',max_length=18,null=False)
    isBan = models.BooleanField(verbose_name='是否禁用',default=False)

    def __str__(self):
        return self.username

 ?STOCK
class Hold(models.Model):
    user = models.ForeignKey(UserInfo)
    stock = models.ForeignKey()
    amount = models.IntegerField(verbose_name='数量')
    price = models.DecimalField(verbose_name='买的价格', max_digits=8, decimal_places=2)
    frozen = models.DecimalField(verbose_name='冻结股票', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.user.username

class Fund(models.Model):
    user = models.OneToOneField(UserInfo,verbose_name='用户')
    money = models.DecimalField(verbose_name='钱',max_digits=8, decimal_places=2)
    frozen_money = models.DecimalField(verbose_name='冻结钱', max_digits=8, decimal_places=2)

    def __str__(self):
        return self.user.username

class Bank(models.Model):
    user = models.ForeignKey(UserInfo)
    realname = models.CharField('真实姓名', max_length=50, null=False)
    bank = models.IntegerField(verbose_name='开户行', choices=BANK_CHOICES, default=0)
    bankNo = models.CharField('银行卡卡号', max_length=50, null=False)
    tradpwd = models.CharField(verbose_name='交易密码', max_length=50, null=False)

    def __str__(self):
        return self.user.username