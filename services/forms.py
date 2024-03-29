from django import forms
from bootstrap_datepicker_plus import TimePickerInput
from .models import Service, Customer, Fuller, Assignservice, Assignservice_detail

class ServiceForms(forms.ModelForm):
    name=forms.CharField(max_length=30,)
    cost=forms.FloatField(help_text='Service Cost in USD')
    class Meta:
        model=Service
        fields=('name','cost')

class CustomerForms(forms.ModelForm):
    age=forms.FloatField(help_text='Age in years')
    class Meta:
        model=Customer
        fields=('name','age','sex','mobile','description')

class FullerForms(forms.ModelForm):
    salary=forms.FloatField(help_text='Salary in USD')
    class Meta:
        model=Fuller
        fields=['name','speciality','salary','days','from_time','to_time']
        widgets = {
            'from_time':TimePickerInput().start_of('party time'),
            'to_time':TimePickerInput().end_of('party time'),
        }

class AssignserviceForm(forms.ModelForm):
    class Meta:
        model=Assignservice
        fields= ('__all__')

class Assignservice_detailForm(forms.ModelForm):
    class Meta:
        fields= ('__all__')
