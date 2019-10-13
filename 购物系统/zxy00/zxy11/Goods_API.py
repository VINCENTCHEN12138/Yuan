from django.http import JsonResponse
from zxy11.models import Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json


def get_Goods(request):
    goodid = request.GET.get('goodid', '')
    goods = {}
    if(goodid == ''):
        result = Goods.objects.all()
        data = []
        for i in result:
            Dict = {}
            Dict['goodid'] = i.goodid
            Dict['amount'] = i.amount
            Dict['Name'] = i.Name
            Dict['purchase'] = i.purchase
            Dict['price'] = i.price
            Dict['goodinfo'] = i.goodinfo
            Dict['pic'] = str(i.pic)
            data.append(Dict)

        return JsonResponse({'status': 200, 'message': 'success', 'data': data})

    result = Goods.objects.get(goodid=goodid)
    if result:
        goods['goodid'] = result.goodid
        goods['amount'] = result.amount
        goods['Name'] = result.Name
        goods['purchase'] = result.purchase
        goods['price'] = result.price
        goods['goodinfo'] = result.goodinfo
        goods['pic'] = str(result.pic)
    else:
        JsonResponse({'status': 0, 'message': 'error'})

    return JsonResponse({'status': 200, 'message': 'success', 'data': goods})
