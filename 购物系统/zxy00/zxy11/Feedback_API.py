from django.http import JsonResponse
from zxy11.models import Feedback,Goods
from django.core.exceptions import ValidationError, ObjectDoesNotExist
import json

def add_Feedback(request):
    userid = request.POST.get('userid', '')
    stars = request.POST.get('stars', '')
    feedback = request.POST.get('feedback', '')
    goodsid = request.POST.get('goodsid','')
    pic = request.FILES['pic']

    if userid == '' or goodsid == ''  or stars == '' or feedback == '':
        return JsonResponse({'status': 10021, 'message': 'not complete'})

    try:
        Feedback.objects.create(userid=userid, goodsid=goodsid,feedback=feedback, stars=stars,pic=pic)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'add_Feedback success!'})

def get_Feedback(request):
    userid = request.GET.get('userid', '')
    if userid == '':
        return JsonResponse({'status': 12001, 'message': 'not exist'})

    if userid != '':
        data = []
        result = Feedback.objects.filter(userid=userid)
        if result:
            for r in result:
                aa = Goods.objects.get(goodid=r.goodsid)
                feedback={}
                feedback['userid'] = r.userid
                feedback['pic'] = str(r.pic)
                feedback['feedback'] = r.feedback
                feedback['stars'] = r.stars
                feedback['id'] = r.id
                feedback['answer']=r.answer
                feedback['Goods']={}
                feedback['Goods']['goodid']=aa.goodid
                data.append(feedback)
            return JsonResponse({'status': 200, 'message': 'success', 'data': data})

def delete_Feedback(request):
    id = request.POST.get('id', '')

    try:
        Feedback.objects.filter(id=id).delete()
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status': 10024, 'message': 'error'})

    return JsonResponse({'status': 300, 'message': 'delete_Feedback success!'})

