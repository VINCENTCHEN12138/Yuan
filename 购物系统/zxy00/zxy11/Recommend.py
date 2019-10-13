from operator import itemgetter
from django.http import JsonResponse
from zxy11.models import BuyHistory,Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json
import sys

#购买此商品的用户还购买了
def get_data(request):
    goodid = request.GET.get('goodid', '')
    if goodid != '':
        data = []
        datas = []
        datass = []
        result = BuyHistory.objects.filter(goodid=goodid)
        if result:
            for r in result:
                data.append(r.userid)
            for i in data:
                results = BuyHistory.objects.filter(userid=i)
                if results:
                    for r1 in results:
                        if r1.goodid !=goodid:
                            b = {}
                            b['gooid']=r1.goodid
                            b['pic']=r1.pic
                            b['Name']=r1.Name
                            datas.append(b)
                            for i in datas:
                                if i not in datass:
                                    datass.append(i)

            return JsonResponse({'status': 200, 'message': 'success', 'data': datass})
#跟商品购买人数推荐
def get_data1(request):
    goodid = request.GET.get('goodid', '')
    if goodid != '':
        data = []
        result = Goods.objects.filter(goodid=goodid)
        if result:
            for r in result:
                a =r.purchase
                b = int(a)
                if b>20:
                    c=r.goodid
                    data.append(c)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})



