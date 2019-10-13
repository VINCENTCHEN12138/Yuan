from django.http import JsonResponse
from zhouxinyuan11.models import user,dingzhixinxi,dizhixinxi
from django.core.exceptions import ValidationError, ObjectDoesNotExist


def add_user(request):

    W_id = request.POST.get('W_id', '')
    Userid = request.POST.get('Userid', '')
    Dingzhi_fk = request.POST.get('Dingzhi_fk', '')
    Address_fk = request.POST.get('Address_fk', '')
    name = request.POST.get('name','')

    if W_id== '' or Userid == '' or Dingzhi_fk == '' or Address_fk == '' or name =='':

        return JsonResponse({'status': 10021, 'message': 'error'})

    result = user.objects.filter(W_id=W_id)
    if result:
        return JsonResponse({'status':10022, 'message': 'error'})

    result = user.objects.filter(Userid=Userid)
    if result:
        return JsonResponse({'status':10023, 'message': 'error'})

    try:
        user.objects.create(W_id=W_id, Userid=Userid,Dingzhi_fk=Dingzhi_fk, Address_fk=Address_fk, name=name)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status':10024, 'message': 'error'})

    return JsonResponse({'status':200, 'message': 'add  success'})




def get_user(request):
    Userid = request.GET.get ('Userid', '')
    if Userid == '' :
        return JsonResponse({'status':12001,'message':'error'})

    if Userid != '':
        users = {}
        try:
            result = user.objects.get(Userid=Userid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':'error'})
        else:
            users['W_id'] = result.W_id
            users['Dingzhi_fk'] = result.Dingzhi_fk
            users['Address_fk'] = result.Address_fk
            users['name']=result.name
            return JsonResponse({'status': 200, 'message': 'success', 'data': users})




def add_dingzhixinxi(request):
    Front_size = request.POST.get('Front_size', '')
    Opposite_size = request.POST.get('Opposite_size', '')
    Front_address = request.POST.get('Front_address', '')
    Opposite_address = request.POST.get('Opposite_address', '')
    Front_coordinate = request.POST.get('Front_coordinate','')
    Opposite_coordinate = request.POST.get('Opposite_coordinate', '')
    design = request.POST.get('design', '')
    color = request.POST.get('color', '')
    category = request.POST.get('category', '')
    W_id = request.POST.get('W_id', '')
    size = request.POST.get('size', '')
    status = request.POST.get('status', '')
    Num = request.POST.get('Num', '')

    if Front_size== '' or Opposite_size == '' or Front_address == '' or Opposite_address == '' or Front_coordinate =='' or Opposite_coordinate =='' or design =='' or color =='' or category =='' or W_id =='' or size =='' or status =='' or Num == '':

        return JsonResponse({'status': 10021, 'message': 'error'})


    try:
        user.objects.create(Front_size=Front_size,Opposite_size=Opposite_size,Front_address=Front_address,Opposite_address=Opposite_address, Front_coordinate=Front_coordinate,Opposite_coordinate=Opposite_coordinate,design=design,color=color,category=category,W_id=W_id,size=size,status=status,Num=Num
)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status':10024, 'message': 'error'})

    return JsonResponse({'status':200, 'message': 'add  success'})



def get_dingzhixinxi(request):
    Userid = request.GET.get ('Userid', '')
    if Userid == '' :
        return JsonResponse({'status':12001,'message':'error'})

    if Userid != '':
        users = {}
        try:
            result = user.objects.get(Userid=Userid)
        except ObjectDoesNotExist:
            return JsonResponse({'status':'error'})
        else:
            users['W_id'] = result.W_id
            users['Dingzhi_fk'] = result.Dingzhi_fk
            users['Address_fk'] = result.Address_fk
            users['name']=result.name
            return JsonResponse({'status': 200, 'message': 'success', 'data': users})

