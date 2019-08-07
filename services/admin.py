from django.contrib import admin
from .models import Service, Customer, Fuller, Assignservice, Assignservice_detail

class AdminService(admin.ModelAdmin):
    model=Service
    list_display=('name','cost')
admin.site.register(Service,AdminService)

class AdminCustomer(admin.ModelAdmin):
    model=Customer
    list_display=('name','age','sex','mobile')
admin.site.register(Customer,AdminCustomer)

class AdminFuller(admin.ModelAdmin):
    model=Fuller
    list_display=('name','speciality','salary','days','from_time','to_time')
admin.site.register(Fuller,AdminFuller)

admin.site.register(Assignservice)
admin.site.register(Assignservice_detail)
