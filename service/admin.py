from django.contrib import admin


from .models import Orders, Service
# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    
    list_display=('service_id','service_name','price','desc')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    
    list_display=('order_id','number','locality','address','date','time','service_name','date_ordered')


# admin.site.register(City)
# admin.site.register(Locality)