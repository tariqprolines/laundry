from django.urls import path
from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('logput',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),

    # Service Views
    path('addservice', views.add_service, name='add-service'),
    path('servicelist', views.service_list, name='service-list'),
    path('editservice/<int:id>', views.edit_service, name='edit-service'),
    path('deleteservice/<int:id>', views.delete_service, name='delete-service'),

    # Customer View
    path('addcustomer', views.add_customer, name='add-customer'),
    path('customerlist', views.customer_list, name='customer-list'),
    path('editcustomer/<int:id>', views.edit_customer, name='edit-customer'),
    path('deletecustomer/<int:id>', views.delete_customer, name='delete-customer'),
    path('assignservice', views.assign_service, name='assign-service'),

    # Fuller View

    path('addfuller', views.add_fuller, name='add-fuller'),
    path('fullerlist', views.fuller_list, name='fuller-list'),
    path('editfuller/<int:id>', views.edit_fuller, name='edit-fuller'),
    path('deletefuller/<int:id>', views.delete_fuller, name='delete-fuller'),
]
