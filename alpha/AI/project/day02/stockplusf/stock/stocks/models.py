from django.db import models
import json
from json.encoder import JSONEncoder
# Create your models here.

class Stock(models.Model):
    stonumber = models.CharField(max_length=20,null=False,verbose_name='股票编码')
    company_name = models.CharField(max_length=64, verbose_name='公司名称')
    industry = models.CharField(blank=True, null=True, max_length=200, verbose_name='细分行业')
    area = models.CharField(max_length=30, blank=True, null=True, verbose_name='地区')
    pe = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='市盈率')
    outstanding = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='流通股本(亿)')
    totals = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='总股本(亿)')
    totalAssets = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='总资产(万)')
    liquidAssets = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='流动资产')
    fixedAssets = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='固定资产')
    reserved = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='公积金')
    reservedPerShare = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='每股公积金')
    esp = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='每股收益')
    bvps = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='每股净资')
    pb = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2, verbose_name='市净率')
    timeToMarket = models.DateField(verbose_name='上市日期')


    def __str__(self):
        return str(self.stonumber)


    def model_to_dict(self):
        stockde = {}
        stockde['stonumber'] = self.stonumber
        stockde['company_name'] = self.company_name
        stockde['industry'] = self.industry
        stockde['area'] = self.area
        stockde['pe'] = str(self.pe)
        stockde['outstanding'] = str(self.outstanding)
        stockde['totals'] = str(self.totals)
        stockde['totalAssets'] = str(self.totalAssets)
        stockde['liquidAssets'] = str(self.liquidAssets)
        stockde['fixedAssets'] = str(self.fixedAssets)
        stockde['reserved'] = str(self.reserved)
        stockde['reservedPerShare'] = str(self.reservedPerShare)
        stockde['esp'] = str(self.esp)
        stockde['bvps'] = str(self.bvps)
        stockde['pb'] = str(self.pb)
        stockde['timeToMarket'] = self.timeToMarket.strftime('%Y-%m-%d %H:%M:%S')
        return stockde


    class Meta:
        db_table = 'Stock'
        verbose_name = '股票信息'
        verbose_name_plural = verbose_name
        ordering = ['-id']


class Link(models.Model):
    title = models.CharField(max_length=50,blank=True, null=True, verbose_name='标题')
    callback_url = models.URLField(blank=True, null=True, verbose_name='url地址')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name
        ordering = ['id']

    def __str__(self):
        return self.title

