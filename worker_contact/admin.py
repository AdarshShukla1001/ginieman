from django.contrib import admin
from django.utils.html import format_html

from .models import WorkingMan

# Register your models here.

@admin.register(WorkingMan)
class WorkersAdmin(admin.ModelAdmin):
    search_fields=('name','phone','phone2','service_names','address')
    list_display=('id','name','phone','phone2','adhar_card','email','service_names','address','image_url')

    def image_url(self, obj):
        return format_html('<a href="%s" target="_blank">%s</a>' % (obj.image_url, "See his image bro"))
    image_url.allow_tags = True

    # def phone(self, obj):
    #     return format_html('<a href="tel:%s">%s</a>' % (obj.phone, "Call"))
    # phone.allow_tags = True

    # def phone2(self, obj):
    #     return format_html('<a href="tel:%s">%s</a>' % (obj.phone2, "Call in second"))
    # phone2.allow_tags = True
    

# def show_firm_url(self, obj):
    # return '<a href="%s">%s</a>' % (obj.firm_url, obj.firm_url)
# show_firm_url.allow_tags = True
    # download_content.allow_tags = True
    # download_content.short_description = "Download Content File"