from django.http import JsonResponse
from zxy11.models import Addressinfo
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json

def add_Addressinfo(request):
    provinceName = request.POST.get('provinceName', '')
    cityName = request.POST.get('cityName', '')
    countyName = request.POST.get('countyName', '')
    detailInfo = request.POST.get('detailInfo', '')
    postalCode = request.POST.get('postalCode', '')
    telNumber = request.POST.get('telNumber', '')
    nationalCode = request.POST.get('nationalCode', '')
    userid = request.POST.get('userid', '')
    userName = request.POST.get('userName', '')

    if provinceName == '' or cityName == '' or countyName == '' or telNumber == '' or userid == '' or userName == '' or detailInfo == '':
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        Addressinfo.objects.create(userid=userid, provinceName=provinceName, postalCode=postalCode, cityName=cityName,
                                   telNumber=telNumber, userName=userName, countyName=countyName, detailInfo=detailInfo,
                                   nationalCode=nationalCode)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_Addressinfo success!'})


def get_Addressinfo(request):
    userid = request.GET.get('userid', '')

    if userid == '':
        return JsonResponse({'status': 12001, 'message': 'not exist'})
    if userid != '':
        data = []
        result = Addressinfo.objects.filter(userid=userid)
        if result:
            for r in result:
                addressinfos={}
                addressinfos['userid'] = r.userid
                addressinfos['provinceName'] = r.provinceName
                addressinfos['cityName'] = r.cityName
                addressinfos['countyName'] = r.countyName
                addressinfos['detailInfo'] = r.detailInfo
                addressinfos['postalCode'] = r.postalCode
                addressinfos['telNumber'] = r.telNumber
                addressinfos['nationalCode'] = r.nationalCode
                addressinfos['userName'] = r.userName
                addressinfos['id'] = r.id
                data.append(addressinfos)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})

def delete_Addressinfo(request):
    id = request.POST.get('id', '')

    try:
        Addressinfo.objects.filter(id=id).delete()
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'delete_Addressinfo success!'})
