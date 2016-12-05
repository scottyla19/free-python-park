from django.shortcuts import render
from dateutil.parser import parse
from datetime import datetime
from django.http import JsonResponse
from django.template import *

def index(request):
    return render(request, 'timestamp/index.html')

def api(request, param_str):

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
        try:
            myDate = datetime.fromtimestamp(int(dateStr))
            natDate = myDate.strftime("%B %-d, %Y")
            unixDate = myDate.strftime('%s')
            jsonArray = {'unix': str(unixDate), 'natural': str(natDate)}
        except ValueError:
            jsonArray = {'unix':None, 'natural':None}

    return JsonResponse(jsonArray)
