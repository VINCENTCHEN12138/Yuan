from django.http import JsonResponse
from zxy11.models import BuyHistory,Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json
#会员等级计算
def get_membership(request):
    userid = request.GET.get('userid','')
    if userid != '':
        data = []
        datas = []

        result = BuyHistory.objects.filter(userid=userid)
        if result:
            for r in result:
                aa = Goods.objects.get(goodid=r.goodid)
                a=r.price
                b=int(a)
                data.append(b)
                c=sum(data)
                d = {}
                if c >=500 :
                    d['membership'] = 1
                    d['price']= 0.95*int(aa.nowprice)
                elif c>=1000:
                    d['membership'] = 2
                    d['price'] = 0.90 * int(aa.nowprice)
                elif c>=2000:
                    d['membership'] = 3
                    d['price'] = 0.85 * int(aa.nowprice)
                elif c>=5000:
                    d['membership'] = 4
                    d['price'] = 0.75 * int(aa.nowprice)
                elif c>=10000:
                    d['membership'] = 5
                    d['price'] = 0.7 * int(aa.nowprice)
                else:
                    d['membership'] = 0
                    d['price'] = aa.nowprice
            datas.append(d)
            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})

