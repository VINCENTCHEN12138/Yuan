import requests
import json
from django.http import JsonResponse
from zxy11.models import User
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import random


def GetOpenid(code):

    Response = requests.get(
        "https://api.weixin.qq.com/sns/jscode2session?appid=wx90f7357f9e5fb100&secret=3d3a56afbcd89742a3bef4a78c649ffb&js_code={code}&grant_type=authorization_code".format(code=code))
    JsonData = json.loads(Response.text)
    print(JsonData)
    if('openid' in JsonData.keys()):
        openid = JsonData['openid']
        return openid

    return 0


def Login(request):

    code = request.GET.get('code', '')

    if(code):
        openid = GetOpenid(code)
        if(openid == 0):
            return JsonResponse({
                'status': 0
            })
        if(User.objects.filter(openid=openid)):
            result = User.objects.get(openid=openid)

            return JsonResponse({
                'status': 200,
                'openid': openid,
                'userid': result.__str__(),
                'address': result.address.__str__()
            })
        else:
            userid = int(random.uniform(1, 99999))
            User.objects.create(openid=openid, userid=userid,address='[]')
            return JsonResponse({
                'status': 200,
                'openid': openid,
                'userid': userid,
                'address': '[]'
            })
