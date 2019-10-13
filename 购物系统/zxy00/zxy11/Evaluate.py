from django.http import JsonResponse
from zxy11.models import Evaluate
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json


def Add(request):
    orderid = request.GET.get('orderid', '')
    text = request.GET.get('text', '')
    Evaluate.objects.create(orderid=orderid, text=text)
    return JsonResponse({
        'status': 200
    })
