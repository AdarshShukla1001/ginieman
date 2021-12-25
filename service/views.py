
import threading
from django.core.mail.message import EmailMessage
from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime

from django.core.mail import send_mail
from django.conf import settings
# import datetime

# from ginieman import service
from .models import Service,Orders, Workers



class EmailThread(threading.Thread):
    def __init__(self, subject, html_content, recipient_list):
        self.subject = subject
        self.recipient_list = recipient_list
        self.html_content = html_content
        threading.Thread.__init__(self)

    def run (self):
        msg = EmailMessage(self.subject, self.html_content, settings.EMAIL_HOST_USER, self.recipient_list)
        #if self.html_content:
        msg.content_subtype='html'
        # msg.attach_alternative(True, "text/html")
        msg.send()



# def send_mail(subject, html_content, recipient_list):
    # EmailThread(subject, html_content, recipient_list).start()


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
        subject = 'GINIE MAN'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email,]
        # send_mail(subject , "Thank for Registring Our Website. Our represtative will contact you before the day Off appointment\n", email_from,recipient_list )
        order = Orders(name=name, email=email, service_name=service_name,number=number,locality=locality,address=address,date=date,time=time,date_ordered=datetime.now())
        order.save()
        # send_mail(subject , "Thank for Registring Our Website. Our represtative will contact you before the day Off appointment\n", email_from,recipient_list )
        # return HttpResponse("message")
        EmailThread(subject, "Thank Your for booking", recipient_list).start()
        return render(request,'mess_order.html')
        
    return HttpResponse('Failed')


def worker(request):
    return render(request,'worker.html')

def worker_register(request):
    if request.method=="POST":
        
        name = request.POST.get('name','')
        # service_name = request.POST.get('service_name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('number', '')
        phone2 = request.POST.get('number2', 0)
        area=request.POST.get('area','')
        service_names=request.POST.get('service')
        # subject = 'GINIE MAN'
        # email_from = settings.EMAIL_HOST_USER
        # send_mail(subject , "Thank for Registring Our Website. Our represtative will contact you before the day Off appointment\n <strong>Thank You</strong>", email_from,  )
        worker = Workers(name=name, email=email, service_names=service_names,area=area,phone2=phone2,phone=phone)
        worker.save()
        return HttpResponse("worker is registered")
    return HttpResponse('failed registration')


def contact(request):
   
    return render(request,'contact_us.html')
