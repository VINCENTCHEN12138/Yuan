# encoding: utf-8
from django.http import JsonResponse
from zhouxinyuan11.models import addressinfo,user,picmake,Orders
from django.core.exceptions import ValidationError,ObjectDoesNotExist

#添加地址信息接口（POST,GET）(待修正)
#POST方法
def add_useraddressinfo(request):
	provinceName = request.POST.get('provinceName','')
	cityName = request.POST.get('cityName','')
	countyName = request.POST.get('countyName','')
	detailInfo = request.POST.get('detailInfo','')
	postalCode = request.POST.get('postalCode','')
	telNumber = request.POST.get('telNumber','')
	nationalCode = request.POST.get('nationalCode','')
	W_id = request.POST.get('W_id','')
	userName = request.POST.get('userName','')


	#报错：内容不完整
	if provinceName == '' or cityName == '' or countyName == '' or telNumber == '' or W_id == '' or userName == '' or detailInfo =='':
		return JsonResponse({'status':10021,'message':'not complete'})
	#查询W_id是否为重复的
	#若重复则用新信息替换原来的信息

	result = addressinfo.objects.filter(W_id=W_id)
	if result:
		addressinfo.objects.filter(W_id=W_id).update(provinceName=provinceName,postalCode=postalCode,cityName=cityName,telNumber=telNumber,userName=userName,countyName=countyName,detailInfo=detailInfo,nationalCode=nationalCode)
		return JsonResponse ({'status':200,'message':'change_useraddressinfo success!'})
	else:
		addressinfo.objects.create(W_id=W_id,provinceName=provinceName,postalCode=postalCode,cityName=cityName,telNumber=telNumber,userName=userName,countyName=countyName,detailInfo=detailInfo,nationalCode=nationalCode)
		return JsonResponse({'status':300,'message':'add_useraddressinfo success!'})
	

#GET方法
def get_useraddressinfo(request):
	W_id = request.GET.get('W_id','')
#报错
	#用户不存在
	if W_id == '':
		return JsonResponse({'status':12001,'message':'not exist'})
	if W_id != '':
		addressinfos = {}
	#异常处理
		try:
			result = addressinfo.objects.get(W_id=W_id)
		except ObjectDoesNotExist:
			return JsonResponse({'status':10022,'message':'empty'})
		else:
			addressinfos['W_id'] = result.W_id
			addressinfos['provinceName'] = result.provinceName
			addressinfos['cityName'] = result.cityName
			addressinfos['countyName'] = result.countyName
			addressinfos['detailInfo'] = result.detailInfo
			addressinfos['postalCode'] = result.postalCode
			addressinfos['telNumber'] = result.telNumber
			addressinfos['nationalCode'] = result.nationalCode
			addressinfos['userName'] = result.userName

			return JsonResponse({'status':200,'message':'success','data':addressinfos})



#添加用户信息接口（post，get）（待修正）
#POST方法
def add_user(request):
	W_id = request.POST.get('W_id','')
	phone = request.POST.get('phone','')
	name = request.POST.get('name','')

#报错
	#若W_id为空
	if W_id == '':
		return JsonResponse({'status':10021,'message':'empty'})
	#若W_id已存在
	result = user.objects.filter(W_id=W_id)
	if result:
		return JsonResponse({'status':10022,'message':'W_id already exist'})
	#异常处理
	try:
		user.objects.create(W_id=W_id,phone=phone,name=name)
	except ValidationError as e:
		error = 'error'
		return JsonResponse({'status':10024,'message':'error'})

	return JsonResponse({'status':200,'message':'add_user success!'})



#GET方法
def get_user(request):
	W_id = request.GET.get('W_id','')
	#若W_id为空
	if W_id == '':
		return JsonResponse({'status':12001,'message':'empty'})
	#若W_id不为空
	if W_id != '':
		users = {}
	#异常处理
	try:
		result = user.objects.get(W_id=W_id)
	except ObjectDoesNotExist:
		return JsonResponse({'status':'error'})
	else:
		users['W_id'] = result.W_id
		users['phone'] = result.phone
		users['name'] = result.name
	return JsonResponse({'status':200,'message':'success','data':users})


#添加商品合成图接口（参数传递post，合成返回用get）
#POST
def add_picmake(request):
	frontx= request.POST.get('frontx','')
	fronty= request.POST.get('fronty','')
	frontpic= request.POST.get('frontpic','')
	oppositex= request.POST.get('oppositex','')
	oppositey= request.POST.get('oppositey','')
	oppositepic= request.POST.get('oppositepic','')
	if frontx =='' or fronty == '' or frontpic == ''or oppositex == '' or oppositey == '' or oppositepic == '':
		return JsonResponse({'status':10021,'message':'not complete'}) 
	
	try:
		picmake.objects.create(frontx=frontx,fronty=fronty,frontpic=frontpic, oppositepic=oppositepic,oppositex=oppositex,oppositey=oppositey)
	except ValidationError as e:
		error = 'error'
		return JsonResponse({'status':10024,'message':'error'})
	return JsonResponse({'status':200,'message':'add_picmake success!'})

#GET
def get_picmakedata(request):
	frontmakepic=request.GET.get('frontmakepic','')
	oppositemakepic=request.GET.get('oppositemakepic','')
	#若正反面合成图为空
	if frontmakepic == '' or opppositemakepic == '':
		return JsonResponse({'status':10021,'message':'empty!'})
	#若正反面合成表不为空
	if frontmakepic != '' or oppositemakepic != '':
		picmakedata = {}
	#异常处理
	try:
		result1 = picmake.objects.get(frontmakepic = frontmakepic)
		result2 = picmake.objects.get(oppositemakepic = oppositemakepic)
	except ObjectDoesNotExist:
		return JsonResponse({'message':'error'})
	else:
		picmakedata['frontmakepic'] = result1.frontmakepic
		picmakedata['oppositemakepic'] = result2.oppositemakepic
		return JsonResponse({'status':200,'message':'success','data':picmakedata})


def add_Orders(request):
	ordernum = request.POST.get('ordernum','')
	goodsid = request.POST.get('goodsid','')
	picid = request.POST.get('picid','')
	addressid = request.POST.get('addressid','')
	userid = request.POST.get('userid','')
	riqi = request.POST.get('riqi','')
	status = request.POST.get('status','')
	expressidnum = request.POST.get('expressidnum','')


	#报错：订单号不可为空
	if ordernum == '':
		return JsonResponse({'status':10021,'message':'ordernum empty'})
	#查询订单号是否为重复的：若重复用新信息替代原来的信息。
	result = Orders.objects.filter(ordernum = ordernum)
	if result:
		Orders.objects.filter(ordernum = ordernum).update(goodsid=goodsid,picid=picid,addressid=addressid,userid=userid,riqi=riqi,status=status,expressidnum=expressidnum)
		return JsonResponse({'status':200,'message':'change add_Orders success!'})
	else:
		Orders.objects.create(ordernum=ordernum,goodsid=goodsid,picid=picid,addressid=addressid,userid=userid,riqi=riqi,status=status,expressidnum=expressidnum)
		return JsonResponse({'status':300,'message':'add add_Orders success!'})


def add_shopping_cart(request):
	userid = request.POST.get('userid','')
	goodsid = request.POST.get('goodsid','')
	picmakeid = request.POST.get('picmakeid','')
	amount = request.POST.get('amount','')

	if userid == '' or goodsid == '' or picmakeid == ''or amount == '':
		return  JsonResponse({'stauts':10021,'messsage':'not complete!'})
	#检查数据是否有更新，若有更新则进行替换，若是第一次生成数据则新建立一个表
	result = shopping_cart.userid(userid = userid)
	if result:
		shopping_cart.objects.filter(userid=userid).update(goodsid=goodsid,picmakeid=picmakeid,amount=amount)
		return JsonResponse({'status':200,'message':'Change shopping_cart success!'})
	else:
		shopping_cart.objects.create(userid=userid,goodsid=goodsid,picmakeid=picmakeid,amount=amount)
		return JsonResponse({'status':300,'message':'Add shopping_cart success!'})
