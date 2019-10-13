from django.http import JsonResponse
from zhouxinyuan11.models import color,design,category,size,goods,Orders,picmake,user,addressinfo,shopping_cart
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json


def get_goods(request):
    goodid = request.GET.get("goodid", "")


    if goodid == '':
        return JsonResponse({'status':12001,'message':'error'})



    if goodid != '':
        Goods = {}
        try:
            result = goods.objects.get(goodid=goodid)
            a = design.objects.get(id=result.designid)
            b = color.objects.get(id=result.colorid)
            c = category.objects.get(id=result.categoryid)
            d = size.objects.get(id=result.sizeid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':'error'})
        else:
            Goods['goodid'] = result.goodid
            Goods['design'] = a.design
            Goods['color'] = b.color
            Goods['category'] = c.category
            Goods['size'] = d.size
            Goods['amount'] = result.amount
            Goods['goodinfo'] = result.goodinfo
            Goods['frontpic'] = result.frontpic
            Goods['oppositpic'] = result.oppositpic
            Goods['Name'] = result.Name
            Goods['nowprice'] = result.nowprice
            Goods['pastprice'] = result.pastprice
            Goods['ontime'] = result.ontime
            Goods['offtime'] = result.offtime
            return JsonResponse({'status': 200, 'message': 'success', 'data': Goods})


def get_Orders(request):
    ordernum = request.GET.get("ordernum", "")
    if ordernum == '':
        return JsonResponse({'status':12001,'message':'error'})
    if ordernum != '':
        datas=[]
        result = Orders.objects.filter(ordernum__contains=ordernum)
        aa = goods.objects.get(id=result.goodsid)
        bb = user.objects.get(id=result.userid)
        cc = addressinfo.objects.get(id=result.addressid)
        if result:
            for r in result:
                a = design.objects.get(id=aa.designid)
                b = color.objects.get(id=aa.colorid)
                c = category.objects.get(id=aa.categoryid)
                d = size.objects.get(id=aa.sizeid)
                e = picmake.objects.get(id=r.picid)
                #c = addressinfo.objects.get(id=r.addressid)
                #d = user.objects.get(id=r.userid)

                orders = {}

                orders['ordernum'] = r.ordernum
                orders['W_id'] = bb.W_id

                orders['goods']={}
                orders['goods']['goodid']=aa.goodid
                orders['goods']['design']=a.design
                orders['goods']['size']=d.size
                orders['goods']['Name'] = aa.Name
                orders['goods']['color'] = b.color
                orders['goods']['category'] = c.category

                #orders['goods']['size'] =
                orders['address']={}
                orders['amount'] = result.amount
                orders['riqi']=result.riqi
                orders['status']=result.status
                orders['expressid']=result.espressid






               #orders['address']=
                datas.append(orders)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})



'''''''''

def get_shoppingcart(request):
    W_id = request.GET.get("W_id", "")
    


    if W_id == '':
        return JsonResponse({'status':12001,'message':'error'})



    if W_id != '':
        datas=[]
        result = user.objects.filter(W_id__contains=W_id)
        aa = shopping_cart.objects.get(userid=result.id)


        if result:
            for r in result:
                a = goods.objects.get(goodid=aa.goodid)
                b = design.objects.get(id=result.designid)
                c = color.objects.get(id=result.colorid)
                d = category.objects.get(id=result.categoryid)
                e = size.objects.get(id=result.sizeid)
                f = goods.objects.get(id=r.goodsid)
                g = picmake.objects.get(id=r.picid)
                #c = addressinfo.objects.get(id=r.addressid)
                #d = user.objects.get(id=r.userid)

                orders = {}
            #b = picmake.objects.get(id=result.picid)
            #c = user.objects.get(id=result.userid)
            #d = addressinfo.objects.get(id=result.addressid)

                #orders['ordernum'] = r.ordernum

                orders['goods']={}
                orders['goods']['goodid']=a.goodid
                orders['goods']['Name']=a.Name
                orders['goods']['frontpic'] =b.frontpic
                orders['goods']['oppositepic'] = b.opposite
                orders['goods']['nowprice'] = a.nowprice
                orders['goods']['frontpic'] = b.frontpic






               #orders['address']=
                datas.append(orders)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})

'''''''''''

''''''''''
def change_Orders(request):
    status = request.POST.get('status', '')
    ordernum = request.GET.get('ordernum','')
    
    
    a= Orders.objects.get()


    if status == '':

        return JsonResponse({'status': 10021, 'message': 'error'})

    result = Orders.objects.filter(status=status)
    if result:
        return JsonResponse({'status':10022, 'message': 'error'})



    return JsonResponse({'status':200, 'message': 'add orders success'})
'''''