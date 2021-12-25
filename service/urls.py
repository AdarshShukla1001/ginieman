from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Home"),
    path("booking/<int:myid>",views.form,name='form'),
    path("success/<int:myid>",views.message,name="message"),
    path('apply/',views.worker,name='apply'),
    path('worker/',views.worker_register,name='registration'),
    
]
