from django.http import JsonResponse
from zxy11.models import Favorites, Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist


def Add(request):
    userid = request.GET.get('userid', '')
    goodid = request.GET.get('goodid', '')
    reslut = Favorites.objects.filter(userid=userid, goodsid=goodid)
    if(reslut):
        return JsonResponse({
            'status': 200
        })

    Favorites.objects.create(userid=userid, goodsid=goodid)
    return JsonResponse({
        'status': 200
    })


def Delete(request):
    userid = request.GET.get('userid', '')
    goodid = request.GET.get('goodid', '')
    print(userid, goodid)
    Favorites.objects.filter(userid=userid, goodsid=goodid).delete()
    return JsonResponse({
        'status': 200
    })


def Get(request):
    userid = request.GET.get('userid', '')
    gooods = []
    usergoods = []
    result = Favorites.objects.filter(userid=userid)
    if(result):
        for i in result:
            usergoods.append(i.goodsid)
        for i in usergoods:
            ret = Goods.objects.filter(goodid=i)
            if(ret):
                for b in ret:
                    Dict = {}
                    print(b)
                    Dict['goodinfo'] = b.goodinfo
                    Dict['pic'] = b.pic.__str__()
                    Dict['price'] = b.price
                    Dict['goodid'] = b.goodid
                    Dict['Name'] = b.Name
                    gooods.append(Dict)
        return JsonResponse({
            'status': 200,
            'gooods': gooods

        })
    else:
        return JsonResponse({
            'status': 0
        })
