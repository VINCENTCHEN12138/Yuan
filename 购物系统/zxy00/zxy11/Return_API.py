from django.http import JsonResponse
from zxy11.models import Return,Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json

def add_Return(request):
    userid = request.POST.get('userid', '')
    goodsid = request.POST.get('goodsid', '')
    amount = request.POST.get('amount', '')


    if userid == '' or goodsid == '' or amount == '' :
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        Return.objects.create(userid=userid, goodsid=goodsid, amount=amount)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_Return success!'})


def get_Return(request):
    userid = request.GET.get('userid', '')
    if userid == '':
        return JsonResponse({'status': 12001, 'message': 'not exist'})

    if userid != '':
        data = []
        result = Return.objects.filter(userid=userid)
        if result:
            for r in result:
                aa = Goods.objects.get(id=r.goodsid)
                REturn={}
                REturn['userid'] = r.userid
                REturn['amount'] = r.amount
                REturn['id'] = r.id
                REturn['Goods']={}
                REturn['Goods']['goodid']=aa.goodid
                REturn['Goods']['design']=aa.design
                REturn['Goods']['size']=aa.size
                REturn['Goods']['Name'] = aa.Name
                REturn['Goods']['color'] = aa.color
                REturn['Goods']['category'] = aa.category
                REturn['Goods']['nowprice'] = aa.nowprice
                REturn['Goods']['pastprice'] = aa.pastprice
                REturn['Goods']['ontime'] = aa.ontime
                REturn['Goods']['offtime'] = aa.offtime
                REturn['Goods']['pic'] = aa.pic
                REturn['Goods']['goodinfo'] = aa.goodinfo
                data.append(REturn)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})


def delete_Return(request):
    id = request.POST.get('id', '')

    try:
        Return.objects.filter(id=id).delete()
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'delete_Return success!'})