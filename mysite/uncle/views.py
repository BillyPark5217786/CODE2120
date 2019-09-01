from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys

# Create your views here.

def seaquest(request, var_a, var_b):
	try:
		returnob = {
		"data": "%s batman: %s chicken!!!" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt
def posts(request):
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			jsob = json.loads(data)

			index =  0
			for i in jsob["demo"]:
				index += 1
			return JsonResponse({"log":log})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("ONLY POST REQUESTS")

@csrf_exempt
def elf(request):
	jsob = {"startNumber":0, "length": 10}
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			recieved = json.loads(data)
			jsob.update(recieved)
			#### Required above this line ####

			startNumber =  int(jsob["startNumber"])
			length = int(jsob["length"])
			loop = range(length)

			numarray = []
			fibno = startNumber
			addno = 1
			for l in loop:
				numarray.append(fibno)
				fibno = fibno+addno
				addno = fibno-addno

			return JsonResponse({"fib":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return JsonResponse(jsob)
