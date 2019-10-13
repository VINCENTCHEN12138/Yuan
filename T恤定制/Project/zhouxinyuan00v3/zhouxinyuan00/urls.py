# encoding: utf-8
"""zhouxinyuan00 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from zhouxinyuan11 import new_jiekou
from fileserver import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^api/add_Orders/', views_if.add_Orders, name='add_Orders'),
    #url(r'^api/get_Orders/', views_if.get_Orders, name='get_Orders'),
    url(r'^api/add_useraddressinfo/',new_jiekou.add_useraddressinfo,name = 'add_useraddressinfo'),
    url(r'^api/get_useraddressinfo/',new_jiekou.get_useraddressinfo,name = 'get_useraddressinfo'),
    url(r'^api/add_user/',new_jiekou.add_user,name = 'add_user'),
    url(r'^api/get_user/',new_jiekou.get_user,name = 'get_user'),
    url(r'^api/add_picmake/',new_jiekou.add_picmake,name = 'add_picmake'),
    url(r'^api/get_picmakedata/',new_jiekou.get_picmakedata,name = 'get_picmakedata'),
    url(r'^index/',views.index),
    url(r'^uploadFile/',views.uploadfile),
]
