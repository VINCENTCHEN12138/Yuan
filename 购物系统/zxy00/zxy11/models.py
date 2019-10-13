from django.db import models

# Create your models here.
# encoding: utf-8
from django.db import models
import PIL


class Orders(models.Model):
    ordernum = models.CharField('订单号', max_length=50)
    goodsid = models.CharField('商品id', max_length=50)
    userid = models.CharField('用户id', max_length=50)
    time = models.DateTimeField('下单时间', auto_now=True)
    status = models.CharField('订单状态', max_length=50)
    expressidnum = models.CharField('快递单号', max_length=50)
    amount = models.CharField('数量', max_length=50, default='')
    addressid = models.CharField('地址表id', max_length=50, default='')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.ordernum


class Favorites(models.Model):
    userid = models.CharField(max_length=50)
    goodsid = models.CharField(max_length=50)

    class Mate:
        verbose_name = '收藏夹'
        verbose_name_plural = verbose_name

    def __str(self):
        return self.userid


class User(models.Model):
    userid = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    openid = models.CharField(max_length=50)
    address = models.CharField(max_length=300)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid


class Goods(models.Model):
    goodid = models.CharField('商品id', max_length=50)
    amount = models.CharField('数量', max_length=50)
    goodinfo = models.TextField('商品详情', max_length=50)
    pic = models.ImageField('商品图片', upload_to='media')
    Name = models.CharField('商品名', max_length=50)
    price = models.CharField('现价', max_length=50)
    purchase = models.CharField('购买人数', max_length=50, default='')

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goodid


class Addressinfo(models.Model):
    provinceName = models.CharField('省份', max_length=50)
    cityName = models.CharField('城市名', max_length=50)
    countyName = models.CharField('区域名', max_length=50)
    detailInfo = models.CharField('具体地址', max_length=50)
    postalCode = models.CharField('邮编', max_length=50)
    telNumber = models.CharField('联系电话', max_length=50)
    userid = models.CharField('用户id', max_length=50, default="")
    nationalCode = models.CharField('国际编码', max_length=50)
    userName = models.CharField('联系人', max_length=50)

    class Meta:
        verbose_name = '地址信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid


class Shopping_cart(models.Model):
    userid = models.CharField('用户id', max_length=50)
    goodsid = models.CharField('商品id', max_length=50)
    amount = models.CharField('数量', max_length=1000)

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid


class Evaluate(models.Model):
    orderid = models.CharField('订单ID', max_length=50)
    text = models.CharField('评论', max_length=200)

    class Matea:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.orderid


class Feedback(models.Model):
    userid = models.CharField('用户id', max_length=50)
    stars = models.CharField('星级', max_length=50)
    feedback = models.CharField('反馈', max_length=50)
    pic = models.ImageField('图片', upload_to='img')
    goodsid = models.CharField('商品表id', max_length=50, default='')
    answer = models.CharField('回复', max_length=50, default='')

    class Meta:
        verbose_name = '信息反馈'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid


class Collector(models.Model):
    userid = models.CharField('用户id', max_length=50)
    goodsid = models.CharField('商品表id', max_length=50)

    class Meta:
        verbose_name = '收藏夹'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid


class History(models.Model):
    userid = models.CharField('用户id', max_length=50)
    goodsid = models.CharField('商品表id', max_length=50)
    time = models.DateTimeField('浏览时间', auto_now=True)

    class Meta:
        verbose_name = '历史记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid


class Return(models.Model):
    userid = models.CharField('用户id', max_length=50)
    goodsid = models.CharField('商品表id', max_length=50)
    amount = models.CharField('数量', max_length=50)

    class Meta:
        verbose_name = '退货'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid


class Change(models.Model):
    userid = models.CharField('用户id', max_length=50)
    oldgoodsid = models.CharField('原商品表id', max_length=50, default="")
    newgoodsid = models.CharField('新商品表id', max_length=50, default="")
    oldamount = models.CharField('原数量', max_length=50, default="")
    newamount = models.CharField('新数量', max_length=50, default="")
    expressidnum = models.CharField('快递单号', max_length=5, default="")

    class Meta:
        verbose_name = '换货'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid


class BuyHistory(models.Model):
    userid = models.CharField('用户id', max_length=50)
    goodid = models.CharField('商品id', max_length=50)
    pic = models.CharField('商品图片', max_length=50, default='')
    Name = models.CharField('商品名', max_length=50, default='')
    price = models.CharField('价格', max_length=50, default='')

    class Meta:
        verbose_name = '历史记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.userid
