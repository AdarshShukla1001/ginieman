
from django.http.response import HttpResponse
from django.shortcuts import render
# import datetime

# from ginieman import service
from .models import Service,Orders, Workers

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

def message(request,myid):
    if request.method=="POST":
        service=Service.objects.filter(service_id=myid)
        name = request.POST.get('name', '')
        # service_name = request.POST.get('service_name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        service_name=service[0].service_name
        # print(service_name)
        number = request.POST.get('number', '')
        locality=request.POST.get('locality','')
        date=request.POST.get('date')
        time=request.POST.get('time')
        
        order = Orders(name=name, email=email, service_name=service_name,number=number,locality=locality,address=address,date=date,time=time)
        order.save()
        return HttpResponse("message")
        
    return HttpResponse('Failed')


def connect(request):
    return render(request,'connect.html')

def worker_register(request):
    if request.method=="POST":
        
        name = request.POST.get('name','')
        # service_name = request.POST.get('service_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('number', '')
        phone2 = request.POST.get('number2', 0)
        area=request.POST.get('area','')
        service_names=request.POST.get('service')
        
        worker = Workers(name=name, email=email, service_names=service_names,area=area,phone2=phone2,phone=phone)
        worker.save()
        return HttpResponse("worker is registered")
    return HttpResponse('failed registration')