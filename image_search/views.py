from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.core import serializers

import requests
from image_search.models import ImageSearch

# Create your views here.
def index(request):
    return render(request, 'image-search/index.html')
def latest(request):
    results = ImageSearch.objects.all().values('created', 'term')
    return JsonResponse({'latest searches': list(results)})

def api(request, search_str = ''):
    offset = request.GET.get('offset')
    if not offset:
        offset = 1
    else:
        offset = int(offset)

    api_url = "https://www.googleapis.com/customsearch/v1?key=%s&cx=%s&q=%s&start=%d&num=10&fields=items(pagemap/cse_image/src,snippet,pagemap/cse_thumbnail/src,link)" % (settings.GOOGLE_API_KEY, settings.GOOGLE_API_CX, search_str, offset)
    r = requests.get(api_url)
    json = r.json()
    data = []
    for i in json['items']:
        tempDict = {'url': i['pagemap']['cse_image'][0]['src'],
                    'thumbnail': i['pagemap']['cse_image'][0]['src'],
                    'link': i['link'],
                    'snippet': i['snippet']
                    }
        data.append(tempDict)

    if len(data) > 0:
        search = ImageSearch(term=search_str )
        search.save()
    return JsonResponse(data, safe = False)
