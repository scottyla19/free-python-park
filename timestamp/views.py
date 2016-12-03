from django.shortcuts import render
from django.http import HttpResponse
from dateutil.parser import parse
from datetime import datetime
from django.http import JsonResponse

def index(request):
    return render(request, 'timestamp/index.html')

def api(request, param_str):
    print (param_str)
    response = getJSON(param_str)
    return response


def getJSON(dateStr):
    jsonArray={}
    try:
        myDate = parse(dateStr)
        natDate = myDate.strftime("%B %-d, %Y")
        unixDate = myDate.strftime('%s')
        jsonArray = {'unix':str(unixDate), 'natural':str(natDate)}
    except ValueError:
        jsonArray = {'unix':None, 'natural':None}

    return JsonResponse(jsonArray)
