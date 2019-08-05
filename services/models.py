from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

class Service(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30,null=True)
    cost=models.FloatField(null=True)
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
class Customer(models.Model):
    Sex_Choice=(
    (1,'Male'),
    (2,'Famale')
    )
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30, null=True)
    age=models.IntegerField()
    sex= models.PositiveSmallIntegerField(choices=Sex_Choice, null= True,)
    mobile=models.CharField(max_length=20, null=True, unique=True)
    description=models.TextField(null=True, blank=True)
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Fuller(models.Model):
    Days_CHOICES = (('Sun', 'Sun'),
              ('Mon', 'Mon'),
              ('Tue', 'Tue'),
              ('Wed', 'Wed'),
              ('Thu', 'Thu'),
              ('Fri', 'Fri'),
              ('Sat', 'Sat'),
              )
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=30, null=True)
    speciality=models.CharField(max_length=30, null=True)
    salary=models.FloatField()
    from_time=models.TimeField(auto_now=False, auto_now_add=False)
    to_time=models.TimeField(auto_now=False, auto_now_add=False)
    days = MultiSelectField(choices=Days_CHOICES)
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name

class Assignservice(models.Model):
    id= models.AutoField(primary_key=True)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    fuller=models.ForeignKey(Fuller, on_delete=models.SET_NULL, null=True)
    total=models.CharField(max_length=100, null=True)
    discount=models.CharField(max_length=100, null=True)
    grandtotal=models.CharField(max_length=100,null=True)
    delivery_date=models.DateField(null=True)

class Assignservice_detail(models.Model):
    id= models.AutoField(primary_key=True)
    assign=models.ForeignKey(Assignservice, on_delete=models.CASCADE)
    service_id=models.IntegerField(null=True)
    quantity=models.IntegerField()
