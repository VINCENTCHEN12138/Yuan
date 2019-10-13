from django.http import JsonResponse
from zxy11.models import Orders, Goods, Addressinfo
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json


def add_Orders(request):
    userid = request.POST.get('userid', '')
    goodsid = request.POST.get('goodsid', '')
    amount = request.POST.get('amount', '')
    ordernum = request.POST.get('ordernum', '')
    addressid = request.POST.get('addressid', '')
    expressidnum = request.POST.get('expressidnum', '')
    status = request.POST.get('status', '')

    if userid == '' or goodsid == '' or amount == '' or ordernum == '' or addressid == '' or expressidnum == ''or status == '':
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        Orders.objects.create(userid=userid, goodsid=goodsid, amount=amount, ordernum=ordernum,
                              addressid=addressid, expressidnum=expressidnum, status=status)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_Orders success!'})


def get_Orders(request):
    userid = request.GET.get('userid', '')
    if userid == '':
        return JsonResponse({'status': 12001, 'message': 'not exist'})

    if userid != '':
        data = []
        result = Orders.objects.filter(userid=userid)
        if result:
            for r in result:
                aa = Goods.objects.get(goodid=r.goodsid)
                orders = {}
                orders['userid'] = r.userid
                orders['amount'] = r.amount
                orders['ordernum'] = r.ordernum
                orders['time'] = r.time
                orders['status'] = r.status
                orders['expressidnum'] = r.expressidnum
                orders['id'] = r.id
                orders['address'] = r.addressid.__str__()
                orders['Goods'] = {}
                orders['Goods']['goodid'] = aa.goodid
                orders['Goods']['Name'] = aa.Name
                orders['Goods']['price'] = aa.price
                orders['Goods']['pic'] = str(aa.pic)
                orders['Goods']['goodinfo'] = aa.goodinfo

                data.append(orders)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})


def Change(request):
    id = request.GET.get('id', '')
    status = request.GET.get('status', '')
    Orders.objects.filter(id=id).update(status=status)
    return JsonResponse({
        'status': 200
    })


def delete_Orders(request):
    id = request.POST.get('id', '')

    try:
        Orders.objects.filter(id=id).delete()
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'delete_Orders success!'})
