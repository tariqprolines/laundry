from django.contrib import admin
from .models import Service, Customer, Fuller, Assignservice, Assignservice_details

admin.site.register(Service)
admin.site.register(Customer)
admin.site.register(Fuller)
admin.site.register(Assignservice)
admin.site.register(Assignservice_details)
