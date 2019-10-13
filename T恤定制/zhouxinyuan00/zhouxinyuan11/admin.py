from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('P_id', 'O_id', 'Name', 'address', 'phone', 'message', 'riqi', 'O_status', 'picture' )


@admin.register(Expressid)
class ExpressidAdmin(admin.ModelAdmin):
    list_display = ('P_id', 'O_id', 'Name', 'expressidnumber', )


