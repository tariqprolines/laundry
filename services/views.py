from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as auth_logout
from .forms import ServiceForms, CustomerForms, FullerForms
from .models import Service, Customer, Fuller
from django.contrib import messages

def index(request):
    if request.method=='POST':
        username= request.POST.get('username')
        password= request.POST.get('password')
        user= authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request,'Username or Password is Wrong')
    return render(request,'services/index.html')
def dashboard(request):
    return render(request,'services/dashboard.html')

def add_service(request):
    if request.method =='POST':
        add_form= ServiceForms(request.POST)
        if add_form.is_valid():
            add_form.save()
            servicename=request.POST.get('name')
            messages.success(request,f'{servicename} service has been added successfully.')
            return redirect('service-list')
        else:
            messages.error(request,'Something Wrong.')
    add_form=ServiceForms()
    return render(request,'services/addservice.html', {'add_form':add_form})

def service_list(request):
    services=Service.objects.all()
    return render(request,'services/servicelist.html',{'services':services})

def edit_service(request,id):
    obj=Service.objects.filter(id=id).first()
    if request.method == 'POST':
        edit_form = ServiceForms(request.POST,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Records have been updated successfully.')
            return redirect('service-list')
    else:
        edit_form=ServiceForms(instance=obj)
    return render(request,'services/editservice.html',{'edit_form':edit_form})

def delete_service(request, id):
    obj=Service.objects.filter(id=id).delete()
    if obj:
        return redirect('service-list')

def add_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForms(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            cname=request.POST.get('name')
            messages.success(request,f'{cname} has been added successfully as customer.')
            return redirect('customer-list')
        else:
            messages.error(request,'Mobile Number Must Unique.')
            return redirect('customer-list')
    customer_form = CustomerForms()
    return render(request,'services/addcustomer.html',{'customer_form':customer_form})
def customer_list(request):
    customers=Customer.objects.all()
    return render(request,'services/customerlist.html',{'customers':customers})

def edit_customer(request,id):
    obj=Customer.objects.filter(id=id).first()
    if request.method == 'POST':
        edit_form = CustomerForms(request.POST,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Records have been updated successfully.')
            return redirect('customer-list')
    else:
        edit_form=CustomerForms(instance=obj)
    return render(request,'services/editcustomer.html',{'edit_form':edit_form})

def delete_customer(request, id):
    obj=Customer.objects.filter(id=id).delete()
    if obj:
        return redirect('customer-list')

def add_fuller(request):
    if request.method == 'POST':
        fuller_form= FullerForms(request.POST)
        if fuller_form.is_valid():
            fuller_form.save()
            fullername=request.POST.get('name')
            messages.success(request, f'{fullername} has been added successfully as Fuller.')
            return redirect('fuller-list')
        else:
            messages.error(request, 'Something Wrong.')
    fuller_form= FullerForms()
    return render(request, 'services/addfuller.html',{'fuller_form':fuller_form})

def fuller_list(request):
    fullers= Fuller.objects.all()
    return render(request,'services/addfuller.html')
def edit_fuller(request,id):
    pass
def delete_fuller(request,id):
    pass
def assign_service(request):
    pass

def logout(request):
    auth_logout(request)
    return redirect('index')
