from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("booking/",views.form,name='form'),
    path("success/",views.message,name="message")
    # path("handlerequest/", views.handlerequest, name="HandleRequest"),

]
