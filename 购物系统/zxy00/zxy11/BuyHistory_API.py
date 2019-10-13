from django.http import JsonResponse
from zxy11.models import BuyHistory,Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json

def add_BuyHistory(request):
    userid = request.POST.get('userid', '')
    goodid = request.POST.get('goodid', '')
    pic = request.POST.get('pic', '')
    Name = request.POST.get('Name', '')
    price = request.POST.get("price",'')



    if userid == '' or goodid == ''or Name == ''or pic == '' or price =='':
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        BuyHistory.objects.create(userid=userid, goodid=goodid, Name=Name, pic=pic,price=price)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_BuyHistory success!'})