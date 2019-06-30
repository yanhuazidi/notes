from django.db import models

# Create your models here.
class Stock(models.Model):
    stonumber = models.CharField('股票编码', max_length=20, null=False)
    company_name = models.CharField('公司名称', max_length=50, null=False)
    industry = models.CharField('细分行业', max_length=50, null=True)
    area = models.CharField('地区', max_length=50, null=True)
    pe = models.DecimalField('市盈率', max_digits=8, decimal_places=2)
    outstanding = models.DecimalField('流通股本', max_digits=8, decimal_places=2)
    totals = models.DecimalField('总股本', max_digits=8, decimal_places=2)
    totalAssets = models.DecimalField('总资产', max_digits=8, decimal_places=2)
    liquidAssets = models.DecimalField('流动资产', max_digits=8, decimal_places=2)
    fixAssets = models.DecimalField('固定资产', max_digits=8, decimal_places=2)
    reserved = models.DecimalField('公积金', max_digits=8, decimal_places=2)
    reservedPerShare = models.DecimalField('每股公积金', max_digits=8, decimal_places=2)
    esp = models.DecimalField('每股收益', max_digits=8, decimal_places=2)
    bvps = models.DecimalField('每股净资', max_digits=8, decimal_places=2)
    pb = models.DecimalField('市净率', max_digits=8, decimal_places=2)
    timeToMarket = models.DateField(verbose_name='上市日期')
    isDelete = models.BooleanField(verbose_name='是否删除',default=False)

    def __str__(self):
        return self.stonumber

class Ad(models.Model):
    title = models.CharField('广告名', max_length=50, null=False)
    callback_url = models.URLField(verbose_name='广告链接')
    adimg = models.ImageField(verbose_name='广告图片', upload_to='img/ad', default='normal.png')
    isDelete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField('标题', max_length=50, null=False)
    body = models.TextField(verbose_name='内容')
    datetime = models.DateTimeField(verbose_name='发布日期', auto_now_add=True)
    isDelete = models.BooleanField(verbose_name='是否删除', default=False)

    def __str__(self):
        return self.title
