# encoding: utf-8
from django.contrib import admin
from .models import *



@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('ordernum', 'goodsid', 'userid', 'time', 'status', 'expressidnum')




@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('goodid','amount','goodinfo','pic','Name','price','id','purchase')


@admin.register(Change)
class ChangeAdmin(admin.ModelAdmin):
    list_display = ('newgoodsid', 'oldgoodsid','newamount', 'oldamount', 'userid', 'expressidnum')

@admin.register(Return)
class ReturnAdmin(admin.ModelAdmin):
    list_display = ('goodsid', 'amount', 'userid')

@admin.register(Evaluate)
class EvaluateAdmin(admin.ModelAdmin):
    list_display = ('orderid',  'text')



