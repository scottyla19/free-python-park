from django.shortcuts import render

from django.http import JsonResponse


def index(request):
    return render(request, 'header/index.html')


def api(request):
    ip = request.META.get('REMOTE_ADDR')
    sw = str(request.META.get('HTTP_USER_AGENT')).split('(')[1].split(')')[0]
    lang = str(request.META.get('HTTP_ACCEPT_LANGUAGE')).split(',')[0]

    return JsonResponse({'ipaddress':ip, 'language':lang, 'software':sw})

