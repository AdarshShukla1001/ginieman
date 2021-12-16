from django.contrib import admin


from .models import Orders, Service, Workers
# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    
    list_display=('service_id','service_name','price','desc')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    search_fields=('order_id','number','locality','address','date','time','service_name','date_ordered')
    list_display=('order_id','number','locality','address','date','time','service_name','date_ordered')

@admin.register(Workers)
class WorkersAdmin(admin.ModelAdmin):
    search_fields=('name','phone','phone2','service_names','area')
    list_display=('id','name','phone','phone2','email','service_names','area')


# admin.site.register(City)
# admin.site.register(Locality)