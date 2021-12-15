from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Service

# Create your views here.
def index(request):
    data=Service.objects.all()
    service={
        "service":data
    }

    # return HttpResponse("Home")
    return render(request,'index.html',service)

def form(request):
    return HttpResponse("form")

def message(request):
    return HttpResponse("message")