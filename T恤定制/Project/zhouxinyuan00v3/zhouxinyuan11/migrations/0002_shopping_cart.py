# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-11-13 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zhouxinyuan11', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shopping_cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=50, verbose_name='用户ID')),
                ('goodsid', models.CharField(max_length=50, verbose_name='商品ID')),
                ('picmakeid', models.CharField(max_length=50, verbose_name='合成图ID')),
                ('amount', models.CharField(max_length=1000, verbose_name='数量')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
    ]
