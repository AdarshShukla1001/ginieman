from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

# from ginieman import service
from .models import Service

# Create your views here.
def index(request):
    data=Service.objects.all()
    service={
        "service":data
    }

    # return HttpResponse("Home")
    return render(request,'index.html',service)

def form(request,myid):
    service=Service.objects.filter(service_id=myid)
    # return HttpResponse("form")
    return render(request,"order.html",{'service':service[0]})

def message(request):
    return HttpResponse("message")