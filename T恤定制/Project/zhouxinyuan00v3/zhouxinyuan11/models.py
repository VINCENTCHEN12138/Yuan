# encoding: utf-8
from django.db import models


class Orders(models.Model):
    ordernum = models.CharField('订单号', max_length=50)
    goodsid = models.CharField('商品表id', max_length=50)
    picid = models.CharField('图片合成表id', max_length=50)
    addressid = models.IntegerField('地址表id', max_length=100)
    userid = models.CharField('用户信息表id', max_length=50)
    riqi = models.DateTimeField('下单时间', auto_now=True)
    status = models.CharField('订单状态', max_length=50)
    expressidnum = models.CharField('快递单号', max_length=50)

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ordernum



class picmake(models.Model):
    frontx = models.CharField('正坐标x', max_length=50)
    fronty = models.CharField('正坐标y', max_length=50)
    frontpic = models.CharField('正面图', max_length=50)
    oppositex = models.CharField('反坐标x', max_length=100)
    oppositey = models.CharField('反坐标y', max_length=50)
    oppositepic = models.CharField('反面图', max_length=50)
    frontmakepic = models.CharField('正面合成图', max_length=50)
    oppositemakepic = models.CharField('反面合成图', max_length=50)

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.frontpic



class user(models.Model):
    W_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.W_id

class  goods(models.Model):
    goodid = models.CharField('商品id', max_length=50)
    design = models.CharField('款式id', max_length=50)
    category = models.CharField('品类id', max_length=50)
    color = models.CharField('颜色id', max_length=50)
    size = models.CharField('尺码id', max_length=50)
    amount = models.CharField('数量', max_length=50)
    goodinfo = models.TextField('商品详情', max_length=50)
    frontpic = models.CharField('正面图片', max_length=50)
    oppositpic = models.CharField('反面图片', max_length=50)
    Name = models.CharField('商品名', max_length=50)
    nowprice = models.CharField('现价', max_length=50)
    pastprice = models.CharField('原价', max_length=50)
    ontime = models.CharField('上架时间', max_length=50)
    offtime = models.CharField('下架时间', max_length=50)

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goodid



class addressinfo(models.Model):
    provinceName = models.CharField('省份', max_length=50)
    cityName = models.CharField('城市名', max_length=50)
    countyName = models.CharField('区域名',max_length=50)
    detailInfo = models.CharField('具体地址',max_length=50)
    postalCode = models.CharField('邮编', max_length=50)
    telNumber = models.CharField('联系电话', max_length=50)
    W_id = models.CharField('ID', max_length=50)
    nationalCode = models.CharField('国际编码',max_length=50)
    userName = models.CharField('联系人', max_length=50)

    class Meta:
        verbose_name = '地址信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.W_id






class color(models.Model):
    color = models.CharField(max_length=50)

    class Meta:
        verbose_name = '颜色'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.color



class design(models.Model):
    design = models.CharField(max_length=50)

    class Meta:
        verbose_name = '款式'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.design


class category(models.Model):
    category = models.CharField(max_length=50)

    class Meta:
        verbose_name = '品类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category


class size(models.Model):
    size = models.CharField(max_length=50)

    class Meta:
        verbose_name = '尺码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.size



class shopping_cart(models.Model):
    userid = models.CharField('用户ID',max_length = 50)
    goodsid = models.CharField('商品ID',max_length = 50)
    picmakeid = models.CharField('合成图ID',max_length = 50)
    amount = models.CharField('数量',max_length = 1000)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.shopping_cart




























