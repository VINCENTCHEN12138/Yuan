# encoding: utf-8
from django.contrib import admin
from .models import *


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('ordernum', 'goodsid', 'picid', 'addressid', 'userid', 'riqi', 'status', 'expressidnum')
