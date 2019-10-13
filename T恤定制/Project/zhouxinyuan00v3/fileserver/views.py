# encoding: utf-8
from django.shortcuts import render,render_to_response,HttpResponse
#from django.views.decorators.csrf import exempt
import os
from django.shortcuts import HttpResponse
#@csrf_exempt

def index(request):
	return render_to_response("index.html")


def uploadfile(request):

	if request.method == "POST":
		file = request.FILES.get("myfile","")
		path = "zhouxinyuan11/static"

		if not os.path.exists(path):
			return HttpResponse("no such path,change your path or make it for me!")

		if not file:
			return HttpResponse("no files for upload!")
		destination = open(os.path.join(path,file.name),"wb")
		for chunk in file.chunks():
			destination.write(chunk)
		destination.close()
	return HttpResponse("success!")











