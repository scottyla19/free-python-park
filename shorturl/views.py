from django.shortcuts import render
from django.utils.crypto import get_random_string
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'shorturl/index.html')

def api(request, new_url):
    #TODO - add rest-framework, create models, create seralizers, save if valid
    uniqueID = get_random_string(length = 6)
    val = URLValidator()
    try:
        val(new_url)
        print("good url")
    except ValidationError:
        print("bad url")
    response = JsonResponse({"original":new_url, "short":uniqueID})
    return response
