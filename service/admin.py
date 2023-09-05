from django.contrib import admin

from service.models import Service

# Register your models here.

class serviceadmin(admin.ModelAdmin):
    list_display=('service_icon','service_title','service_desc')

admin.site.register(Service)