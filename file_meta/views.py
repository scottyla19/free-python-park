from django.shortcuts import render
from django.http import JsonResponse
from .forms import FileForm
from django.http import HttpResponseRedirect
import os

def get_file_size(f):
    # try:
    #     st = os.path.getsize(f)
    # except TypeError:
    #     return {'error':"failed to get information about"}
    # else:
    return  {"file size": f}

def api(request, data):

    return JsonResponse({'size':data})

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Your code for POST
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            data = request.FILES['file'].size
            return HttpResponseRedirect('/file-meta/api/%s' % data)
    else:
        form = FileForm()

    return render(request, 'file-meta/index.html', {'form':form})

