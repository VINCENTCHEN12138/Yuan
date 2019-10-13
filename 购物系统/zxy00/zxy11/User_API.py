from django.http import JsonResponse
from zxy11.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json

def add_User(request):
    userid = request.POST.get('userid', '')
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')
    openid= request.POST.get('openid','')

    if userid == '' or phone == '' or name == '' or openid=='' :
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        User.objects.create(userid=userid, phone=phone, name=name,openid=openid)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_User success!'})


def get_User(request):
    userid = request.GET.get('userid', '')

    if userid == '':
        return JsonResponse({'status': 12001, 'message': 'not exist'})
    if userid != '':
        data = []
        result = User.objects.filter(userid=userid)
        if result:
            for r in result:
                user={}
                user['userid'] = r.userid
                user['name'] = r.name
                user['phone'] = r.phone
                user['openid']=r.openid
                data.append(user)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})
        else:
            return JsonResponse({'status':0,'message':'not find userid'})


def change_User(request):
    userid = request.POST.get('userid', '')
    name = request.POST.get('name', '')
    phone = request.POST.get('phone', '')

    if userid == '' or phone == '' or name == '':
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    result = User.objects.filter(userid=userid)
    if result:
        User.objects.filter(userid=userid).update(name=name,phone=phone)
        return JsonResponse({'status': 200, 'message': 'change_User success!'})


