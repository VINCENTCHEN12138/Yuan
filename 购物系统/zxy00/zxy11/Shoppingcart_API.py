from django.http import JsonResponse
from zxy11.models import Shopping_cart, Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json


def add_Shoppingcart(request):
    userid = request.POST.get('userid', '')
    goodsid = request.POST.get('goodsid', '')
    amount = request.POST.get('amount', '')
    print(userid, goodsid, amount)

    if userid == '' or goodsid == '' or amount == '':
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        Shopping_cart.objects.create(
            userid=userid, goodsid=goodsid, amount=amount)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_Shoppingcart success!'})


def get_Shoppingcart(request):
    userid = request.GET.get('userid', '')
    if userid == '':
        return JsonResponse({'status': 12001, 'message': 'not exist'})

    if userid != '':
        data = []
        result = Shopping_cart.objects.filter(userid=userid)
        if result:
            for r in result:
                aa = Goods.objects.get(goodid=r.goodsid)
                shoppingcart = {}
                shoppingcart['userid'] = r.userid
                shoppingcart['amount'] = r.amount
                shoppingcart['id'] = r.id
                shoppingcart['Goods'] = {}
                shoppingcart['Goods']['goodid'] = aa.goodid
                shoppingcart['Goods']['Name'] = aa.Name
                shoppingcart['Goods']['price'] = aa.price
                shoppingcart['Goods']['pic'] = str(aa.pic)
                shoppingcart['Goods']['goodinfo'] = aa.goodinfo
                data.append(shoppingcart)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})
        else:
            return JsonResponse({'status': 0, 'message': 'not goods'})


def delete_Shoppingcart(request):
    id = request.POST.get('id', '')
    try:
        Shopping_cart.objects.filter(id=id).delete()
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'delete_Shoppingcart success!'})
