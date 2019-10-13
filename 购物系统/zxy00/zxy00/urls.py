"""zxy URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from zxy11 import Goods_API
from zxy11 import Addressinfo_API
from zxy11 import User_API
from zxy11 import Shoppingcart_API
from zxy11 import Collector_API
from zxy11 import Return_API
from zxy11 import Orders_API
from zxy11 import Feedback_API
from zxy11 import Change_API
from zxy11 import History_API
from zxy11 import BuyHistory_API
from zxy11 import Recommend
from zxy11 import Statistics
from zxy11 import Membership
from zxy11 import Login
from zxy11 import Favorites
from zxy11 import Evaluate
from django.conf import settings
from django.views.static import serve
from zxy11 import ChangeAddress


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/get_Goods/', Goods_API.get_Goods, name='get_Goods'),
    url(r'^api/add_Addressinfo/',
        Addressinfo_API.add_Addressinfo, name='add_Addressinfo'),
    url(r'^api/get_Addressinfo/',
        Addressinfo_API.get_Addressinfo, name='get_Addressinfo'),
    url(r'^api/delete_Addressinfo/',
        Addressinfo_API.delete_Addressinfo, name='delete_Addressinfo'),
    url(r'^api/add_User/', User_API.add_User, name='add_User'),
    url(r'^api/get_User/', User_API.get_User, name='get_User'),
    url(r'^api/change_User/', User_API.change_User, name='change_User'),
    url(r'^api/add_Shoppingcart/',
        Shoppingcart_API.add_Shoppingcart, name='add_Shoppingcart'),
    url(r'^api/get_Shoppingcart/',
        Shoppingcart_API.get_Shoppingcart, name='get_Shoppingcart'),
    url(r'^api/delete_Shoppingcart/',
        Shoppingcart_API.delete_Shoppingcart, name='delete_Shoppingcart'),
    url(r'^api/add_Collector/', Collector_API.add_Collector, name='add_Collector'),
    url(r'^api/get_Collector/', Collector_API.get_Collector, name='get_Collector'),
    url(r'^api/delete_Collector/',
        Collector_API.delete_Collector, name='delete_Collector'),
    url(r'^api/add_Return/', Return_API.add_Return, name='add_Return'),
    url(r'^api/get_Return/', Return_API.get_Return, name='get_Return'),
    url(r'^api/delete_Return/', Return_API.delete_Return, name='delete_Return'),
    url(r'^api/add_Orders/', Orders_API.add_Orders, name='add_Orders'),
    url(r'^api/get_Orders/', Orders_API.get_Orders, name='get_Orders'),
    url(r'^api/delete_Orders/', Orders_API.delete_Orders, name='delete_Orders'),
    url(r'^api/add_Feedback/', Feedback_API.add_Feedback, name='add_Feedback'),
    url(r'^api/get_Feedback/', Feedback_API.get_Feedback, name='get_Feedback'),
    url(r'^api/delete_Feedback/',
        Feedback_API.delete_Feedback, name='delete_Feedback'),
    url(r'^api/add_Change/', Change_API.add_Change, name='add_Change'),
    url(r'^api/get_Change/', Change_API.get_Change, name='get_Change'),
    url(r'^api/delete_Change/', Change_API.delete_Change, name='delete_Change'),
    url(r'^api/add_History/', History_API.add_History, name='add_History'),
    url(r'^api/get_History/', History_API.get_History, name='get_History'),
    url(r'^api/delete_History/', History_API.delete_History, name='delete_History'),
    url(r'^api/add_BuyHistory/', BuyHistory_API.add_BuyHistory, name='add_BuyHistory'),
    url(r'^api/Recommend/', Recommend.get_data, name='Recommend'),
    url(r'^api/Recommend1/', Recommend.get_data1, name='Recommend1'),
    url(r'^api/Statistics/', Statistics.get_data, name='Statistics'),
    url(r'^api/Membership/', Membership.get_membership, name='Membership'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    url(r'api/Login/', Login.Login, name='Login'),
    url(r'api/ChangeAddress', ChangeAddress.Change, name='ChangeAddress'),
    url(r'api/GetFavorites', Favorites.Get, name="Get"),
    url(r'api/DeleteFavorites', Favorites.Delete, name="Delete"),
    url(r'api/AddFavorites', Favorites.Add, name="Add"),
    url(r'api/AddEvaluate', Evaluate.Add, name='AddEvaluate'),
    url(r'api/ChangeOrder', Orders_API.Change,name="change")

]
