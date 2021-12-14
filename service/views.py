from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Home")
    return render(request,'index.html')

def form(request):
    return HttpResponse("form")

def message(request):
    return HttpResponse("message")