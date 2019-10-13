from django.http import JsonResponse
from zxy11.models import History,Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json

def add_History(request):
    userid = request.POST.get('userid', '')
    goodsid = request.POST.get('goodsid', '')



    if userid == '' or goodsid == '' :
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        History.objects.create(userid=userid, goodsid=goodsid)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_History success!'})

def get_History(request):
    userid = request.GET.get('userid', '')
    if userid == '':
        return JsonResponse({'status': 12001, 'message': 'not exist'})

    if userid != '':
        data = []
        result = History.objects.filter(userid=userid)
        if result:
            for r in result:
                aa = Goods.objects.get(id=r.goodsid)
                history={}
                history['userid'] = r.userid
                history['time']=r.time
                history['id'] = r.id
                history['Goods']={}
                history['Goods']['goodid']=aa.goodid
                history['Goods']['design']=aa.design
                history['Goods']['size']=aa.size
                history['Goods']['Name'] = aa.Name
                history['Goods']['color'] = aa.color
                history['Goods']['category'] = aa.category
                history['Goods']['nowprice'] = aa.nowprice
                history['Goods']['pastprice'] = aa.pastprice
                history['Goods']['ontime'] = aa.ontime
                history['Goods']['offtime'] = aa.offtime
                history['Goods']['pic'] = aa.pic
                history['Goods']['goodinfo'] = aa.goodinfo
                history['Goods']['amount'] = aa.amount
                data.append(history)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})

def delete_History(request):
    id = request.POST.get('id', '')

    try:
        History.objects.filter(id=id).delete()
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'delete_History success!'})