from django import forms
from .models import Service, Customer, Fuller

class ServiceForms(forms.ModelForm):
    name=forms.CharField(max_length=30,)
    cost=forms.FloatField(help_text='Service Cost in USD')
    class Meta:
        model=Service
        fields=('name','cost')

class CustomerForms(forms.ModelForm):
    class Meta:
        model=Customer
        fields=('name','age','sex','mobile','description')

class FullerForms(forms.ModelForm):
    from_time=forms.TimeField()
    to_time=forms.TimeField()
    salary=forms.FloatField(help_text='Salary in USD')
    class Meta:
        model=Fuller
        fields=('__all__')
