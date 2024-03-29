from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone as tz
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import ServiceForms, CustomerForms, FullerForms, AssignserviceForm, Assignservice_detailForm
from .models import Service, Customer, Fuller, Assignservice, Assignservice_detail
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
@login_required(login_url='/')
def dashboard(request):
    return render(request,'services/dashboard.html')

@login_required(login_url='/')
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

@login_required(login_url='/')
def service_list(request):
    services=Service.objects.all().order_by('-id')
    return render(request,'services/servicelist.html',{'services':services})

@login_required(login_url='/')
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

@login_required(login_url='/')
def delete_service(request, id):
    obj=Service.objects.filter(id=id).delete()
    if obj:
        return redirect('service-list')

@login_required(login_url='/')
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

@login_required(login_url='/')
def customer_list(request):
    customers=Customer.objects.all().order_by('-id')
    return render(request,'services/customerlist.html',{'customers':customers})

@login_required(login_url='/')
def edit_customer(request,id):
    obj=Customer.objects.filter(id=id).first() #  get single objects
    if request.method == 'POST':
        edit_form = CustomerForms(request.POST,instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Records have been updated successfully.')
            return redirect('customer-list')
    else:
        edit_form=CustomerForms(instance=obj)
    return render(request,'services/editcustomer.html',{'edit_form':edit_form})

@login_required(login_url='/')
def delete_customer(request, id):
    obj=Customer.objects.filter(id=id).delete()
    if obj:
        return redirect('customer-list')

@login_required(login_url='/')
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

@login_required(login_url='/')
def fuller_list(request):
    fullers= Fuller.objects.all().order_by('-id')
    return render(request,'services/fullerlist.html',{'fullers':fullers})

@login_required(login_url='/')
def edit_fuller(request,id):
    obj=Fuller.objects.filter(id=id).first() # get single objects
    if request.method == 'POST':
        edit_form= FullerForms(request.POST, instance=obj)
        if edit_form.is_valid():
            edit_form.save()
            messages.success(request, 'Fuller has been updated successfully.')
            return redirect('fuller-list')
    else:
        edit_form = FullerForms(instance=obj)
    return render(request, 'services/editfuller.html',{'edit_form':edit_form})

@login_required(login_url='/')
def delete_fuller(request,id):
    delfuller=Fuller.objects.filter(id=id).delete()
    if delfuller:
        return redirect('fuller-list')

@login_required(login_url='/')
def assign_service(request):
    services=Service.objects.all()
    customers=Customer.objects.all()
    fullers=Fuller.objects.all()
    data={'customers':customers,'fullers':fullers, 'services':services}
    if request.method == 'POST':
        customer_id=request.POST.get('customer_id')
        fuller_id=request.POST.get('fuller_id')
        total=request.POST.get('totalinput')
        discount=request.POST.get('discount')
        grandtotal=request.POST.get('gtotalinput')
        delivery_date=request.POST.get('delivery_date')
        assignservice=Assignservice(customer_id=customer_id,fuller_id=fuller_id,total=total,discount=discount,grandtotal=grandtotal,delivery_date=delivery_date);
        assignservice.save()
        assign_service=request.POST.getlist('service[]')
        id = Assignservice.objects.latest('id') # get last inserted id
        assign_id=id.id
        status=False
        for i in assign_service:
            print(assign_id)
            service_id=i
            quantity=request.POST.get('q'+i)
            assignervice_detail=Assignservice_detail(service_id=service_id,quantity=quantity,assign_id=assign_id)
            assignervice_detail.save()
            status=True
        if status==True:
            messages.success(request, 'Assign services successfully to customer.')
        else:
            message.error('Somethong Wrong.')

    return render(request,'services/assignservice.html',data)

@login_required(login_url='/')
def invoice_list(request):
    assign_services=Assignservice.objects.all().order_by('-id')
    return render(request,'services/invoicelist.html',{'assign_services':assign_services})

@login_required(login_url='/')
def view_invoice(request,id):
    assign_services=Assignservice.objects.filter(id=id)
    today_date=tz.now();
    assign_service_details=Assignservice_detail.objects.filter(assign_id=id)
    return render(request,'services/viewinvoice.html',{'assign_services':assign_services,'today_date':today_date,'assign_service_details':assign_service_details})

@login_required(login_url='/')
def delete_invoice(request,id):
    delassignservice=Assignservice.objects.filter(id=id).delete()
    if delassignservice:
        return redirect('invoice-list')

def logout(request):
    auth_logout(request)
    return redirect('index')
