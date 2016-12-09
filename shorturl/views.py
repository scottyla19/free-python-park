from django.shortcuts import render
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.shortcuts import redirect
from shorturl.models import ShortUrl
from django.contrib.sites.shortcuts import get_current_site


# Create your views here.
def index(request):
    return render(request, 'shorturl/index.html')

def visit(request, visit_url):
    short = ShortUrl.objects.filter(unique_id = visit_url).values()[0]
    return redirect(short["original_url"])

def api(request, new_url):
    val = URLValidator()
    try:
        val(new_url)
        current_site = get_current_site(request)
        url = ShortUrl(original_url=new_url, base_url=request.META['HTTP_HOST'] + "/shorturl/")
        url.save()
        return JsonResponse({'original_url':url.original_url,'short_url':url.short_url })
    except ValidationError:
        return JsonResponse({"error":"Invalid URL"})
