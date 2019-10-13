from django.http import JsonResponse
from zxy11.models import Addressinfo
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json
from zxy11.models import User


def Change(request):
    address = request.GET.get("address", '')
    openid = request.GET.get('openid', '')

    User.objects.filter(openid=openid).update(address=address)

    return JsonResponse({
        'status': 200
    })
