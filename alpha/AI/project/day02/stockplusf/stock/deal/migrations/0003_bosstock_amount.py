# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-30 01:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deal', '0002_auto_20180913_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='bosstock',
            name='amount',
            field=models.IntegerField(default=0, verbose_name='买卖数量'),
            preserve_default=False,
        ),
    ]
