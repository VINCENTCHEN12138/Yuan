from django.http import JsonResponse
from zhouxinyuan11.models import Orders
from django.core.exceptions import ValidationError, ObjectDoesNotExist


def add_Orders(request):
    P_id = request.POST.get('P_id', '')
    O_id = request.POST.get('O_id', '')
    Name = request.POST.get('Name', '')
    address = request. POST. get('address', '')
    phone = request.POST.get('phone', '')
    message = request.POST.get('message', '')
    riqi = request.POST.get('riqi', '')
    O_status = request.POST.get('O_status', '')
    picture = request.POST.get('picture', '')

    if P_id == '' or O_id == '' or Name == '' or address == '' or phone == '' or message == '' or riqi == '' or O_status == '' or picture == '':

        return JsonResponse({'status': 10021, 'message': 'error'})

    result = Orders.objects.filter(P_id=P_id)
    if result:
        return JsonResponse({'status':10022, 'message': 'error'})

    result = Orders.objects.filter(Name=Name)
    if result:
        return JsonResponse({'status':10023, 'message': 'error'})

    try:
        Orders.objects.create(P_id=P_id, Name=Name, O_id=O_id, address=address, phone=phone, message=message, riqi=riqi, O_status=O_status,picture=picture)
    except ValidationError as e:
        error = 'error'
        return JsonResponse({'status':10024, 'message': 'error'})

    return JsonResponse({'status':200, 'message': 'add orders success'})


def get_Orders(request):
    P_id = request.GET.get ("P_id", "")
    Name = request.GET.get('Name', '')
    if P_id == '' and Name == '':
        return JsonResponse({'status':12001,'message':'error'})

    if P_id != '':
        orders = {}
        try:
            result = Orders.objects.get(P_id=P_id)
        except ObjectDoesNotExist:
            return JsonResponse({'status':'error'})
        else:
            orders['O_id'] = result.O_id
            orders['Name'] = result.Name
            orders['O_status'] = result.O_status
            orders['address'] = result.address
            orders['phone'] = result.phone
            orders['message'] = result.message
            orders['riqi'] = result.riqi
            orders['picture'] = result.picture
            return JsonResponse({'status': 200, 'message': 'success', 'data': orders})

    if Name != '':
        datas=[]
        results = Orders.objects.filter(name__contains=Name)
        if results:
            for r in results:
                orders = { }
                orders['Name'] = r.Name
                orders['O_id'] = r.O_id
                orders['O_status'] = r.O_status
                orders['address'] = r.address
                orders['phone'] = r.phone
                orders['message'] = r.message
                orders['riqi'] = r.riqi
                orders['picture'] = r.picture
                datas.append(orders)
            return JsonResponse ({'status':200,'message':'success', 'data':datas})
        else:
            return JsonResponse({'status':10022,'message':'empty'})



