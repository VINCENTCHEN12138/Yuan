from django.http import JsonResponse
from zxy11.models import Collector,Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json

def add_Collector(request):
    userid = request.POST.get('userid', '')
    goodsid = request.POST.get('goodsid', '')


    if userid == '' or goodsid == '':
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        Collector.objects.create(userid=userid, goodsid=goodsid)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_Collector success!'})

def get_Collector(request):
    userid = request.GET.get('userid', '')
    if userid == '':
        return JsonResponse({'status': 12001, 'message': 'not exist'})

    if userid != '':
        data = []
        result = Collector.objects.filter(userid=userid)
        if result:
            for r in result:
                aa = Goods.objects.get(id=r.goodsid)
                collector={}
                collector['userid'] = r.userid
                collector['id'] = r.id
                collector['Goods']={}
                collector['Goods']['goodid']=aa.goodid
                collector['Goods']['design']=aa.design
                collector['Goods']['size']=aa.size
                collector['Goods']['Name'] = aa.Name
                collector['Goods']['color'] = aa.color
                collector['Goods']['category'] = aa.category
                collector['Goods']['nowprice'] = aa.nowprice
                collector['Goods']['pastprice'] = aa.pastprice
                collector['Goods']['ontime'] = aa.ontime
                collector['Goods']['offtime'] = aa.offtime
                collector['Goods']['pic'] = aa.pic
                collector['Goods']['goodinfo'] = aa.goodinfo
                collector['Goods']['amount'] = aa.amount
                data.append(collector)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})

def delete_Collector(request):
    id = request.POST.get('id', '')

    try:
        Collector.objects.filter(id=id).delete()
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'delete_Collector success!'})