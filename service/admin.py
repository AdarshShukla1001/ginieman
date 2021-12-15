from django.contrib import admin


from .models import City, Locality, Service
# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    
    list_display=('service_id','service_name','price','desc')

admin.site.register(City)
admin.site.register(Locality)