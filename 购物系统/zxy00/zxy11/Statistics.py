from operator import itemgetter
from django.http import JsonResponse
from zxy11.models import BuyHistory
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json
#统计购买人数
def get_data(request):
    goodid = request.GET.get('goodid', '')
    if goodid != '':
        data = []
        datas = []

        result = BuyHistory.objects.filter(goodid=goodid)
        if result:
            for r in result:
                data.append(r.userid)
            a = len(data)
            datas.append(a)


            return JsonResponse({'status': 200, 'message': 'success', 'data': datas})
