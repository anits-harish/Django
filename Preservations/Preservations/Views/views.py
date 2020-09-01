from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #html = "<html><body>Index Page</body></html>"
    #return HttpResponse('template/index.html')
    return render(request,'index.html')