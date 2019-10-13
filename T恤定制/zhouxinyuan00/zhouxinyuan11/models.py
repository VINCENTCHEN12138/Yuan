from django.db import models


class Orders(models.Model):
    P_id = models.CharField('账号', max_length=50)
    O_id = models.CharField('订单号', max_length=50)
    Name = models.CharField('姓名', max_length=50)
    address = models.CharField('地址', max_length=100)
    phone = models.CharField('手机号', max_length=50)
    message = models.CharField('信息', max_length=50)
    riqi = models.CharField('日期', max_length=50)
    O_status = models.CharField('订单状态', max_length=50)
    picture = models.CharField('图片', max_length=10000)

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name

class Expressid(models.Model):
    P_id = models.CharField('账号', max_length=50)
    O_id = models.CharField('订单号', max_length=50)
    Name = models.CharField('姓名', max_length=50)
    expressidnumber = models.CharField('快递号', max_length=50)

    class Meta:
        verbose_name = '发货'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Name

class user(models.Model):
    W_id = models.CharField(max_length=50)
    Userid = models.CharField(max_length=50)
    Dingzhi_fk = models.CharField(max_length=50)
    Address_fk = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.W_id

class  dingzhixinxi(models.Model):
    Front_size = models.CharField('正面大小', max_length=50)
    Opposite_size = models.CharField('反面大小', max_length=50)
    Front_address = models.CharField('正面地址', max_length=50)
    Opposite_address = models.CharField('反面地址', max_length=50)
    Front_coordinate = models.CharField('正面坐标', max_length=50)
    Opposite_coordinate = models.CharField('反面坐标', max_length=50)
    design = models.CharField('款式', max_length=50)
    color = models.CharField('颜色', max_length=50)
    category = models.CharField('品类', max_length=50)
    W_id = models.CharField('ID', max_length=50)
    size = models.CharField('大小', max_length=50)
    staus = models.CharField('订单状态', max_length=50)
    Num = models.CharField('数量', max_length=50)

    class Meta:
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Id

class dizhixinxi(models.Model):
    Address = models.CharField('地址', max_length=50)
    postalCode = models.CharField('邮编', max_length=50)
    detailInfo = models.CharField('说明', max_length=50)
    telNum = models.CharField('联系电话', max_length=50)
    W_id = models.CharField('ID', max_length=50)
    Name = models.CharField('用户姓名', max_length=50)

    class Meta:
        verbose_name = '地址信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Id















































