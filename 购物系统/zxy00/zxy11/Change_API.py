from django.http import JsonResponse
from zxy11.models import Change,Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json

def add_Change(request):
    userid = request.POST.get('userid', '')
    oldgoodsid = request.POST.get('oldgoodsid', '')
    newgoodsid = request.POST.get('newgoodsid', '')
    oldamount = request.POST.get('oldamount', '')
    newamount = request.POST.get('newamount', '')


    if userid == '' or oldgoodsid == '' or oldamount == '' or newamount == '' or newgoodsid == '':
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        Change.objects.create(userid=userid, oldgoodsid=oldgoodsid, oldamount=oldamount, newamount=newamount, newgoodsid=newgoodsid)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_Change success!'})

def get_Change(request):
    userid = request.GET.get('userid', '')
    if userid == '':
        return JsonResponse({'status': 12001, 'message': 'not exist'})

    if userid != '':
        data = []
        result = Change.objects.filter(userid=userid)
        if result:
            for r in result:
                aa = Goods.objects.get(id=r.oldgoodsid)
                bb = Goods.objects.get(id=r.newgoodsid)
                change={}
                change['userid'] = r.userid
                change['oldamount'] = r.oldamount
                change['newamount'] = r.newamount
                change['oldgoodsid'] = r.oldgoodsid
                change['newamount'] = r.newgoodsid
                change['expressidnum'] = r.expressidnum
                change['id'] = r.id
                change['oldGoods']={}
                change['oldGoods']['goodid']=aa.goodid
                change['oldGoods']['design']=aa.design
                change['oldGoods']['size']=aa.size
                change['oldGoods']['Name'] = aa.Name
                change['oldGoods']['color'] = aa.color
                change['oldGoods']['category'] = aa.category
                change['oldGoods']['nowprice'] = aa.nowprice
                change['oldGoods']['pastprice'] = aa.pastprice
                change['oldGoods']['ontime'] = aa.ontime
                change['oldGoods']['offtime'] = aa.offtime
                change['oldGoods']['pic'] = aa.pic
                change['oldGoods']['goodinfo'] = aa.goodinfo
                change['newGoods']={}
                change['newGoods']['goodid']=bb.goodid
                change['newGoods']['design']=bb.design
                change['newGoods']['size']=bb.size
                change['newGoods']['Name'] = bb.Name
                change['newGoods']['color'] = bb.color
                change['newGoods']['category'] = bb.category
                change['newGoods']['nowprice'] = bb.nowprice
                change['newGoods']['pastprice'] = bb.pastprice
                change['newGoods']['ontime'] = bb.ontime
                change['newGoods']['offtime'] = bb.offtime
                change['newGoods']['pic'] = bb.pic
                change['newGoods']['goodinfo'] = bb.goodinfo
                data.append(change)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})

def delete_Change(request):
    id = request.POST.get('id', '')

    try:
        Change.objects.filter(id=id).delete()
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'delete_Change success!'})