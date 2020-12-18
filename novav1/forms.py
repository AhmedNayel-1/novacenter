from django import forms

from django_select2 import forms as s2forms

from . import models
from novav1.models import Packages

from django.forms.widgets import *
from crispy_forms.layout import *
from crispy_forms.helper import *
from django.template import Template, Context
from django.forms.widgets import DateInput, TextInput ,DateTimeBaseInput ,TimeInput

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class PatientNameWidget(s2forms.ModelSelect2Widget):
    search_fields = ["PatientName__istartswith",]


# class PatientMobileAuthorsWidget(s2forms.ModelSelect2MultipleWidget):
#     search_fields =  ["PatientName__istartswith", "PatientMobile1__icontains"]


class PatientForm(forms.ModelForm):
    class Meta:
        model = models.Patient
        # fields = ['PatientName','Gender','PatientMobile1','PatientMobile2','ComeFrom',
        #    'PatientFfriend','Birtdate','PatientCode','Jop','Area','Active','PatientPackages']
        fields="__all__"
        # widgets = {
        #     'Birtdate': DateInput(attrs={'type': 'date'}),}
            
        # labels = {
        #     'PatientName': ('x'),
        #     'Gender': (''),
        #     'Active': (''),
        #     'PatientBbarcode': (''),
        #     'Birtdate': (''),
        #     'ComeFrom': (''),
        #     'PatientFfriend': (''),
        #     'doctor': (''),
        #     'Jop': (''),
        #     'Area': (''),
        #     'PatientMobile1': (''),
        #     'PatientMobile2': ('')
            
            
        #     },

        # help_texts = {
        #                         'PatientName': ('اسم العميل'),
        #                         'Gender': ('النوع'),
        #                         'Active': (''),
        #                         'PatientBbarcode': (''),
        #                         'Birtdate': (''),
        #                         'ComeFrom': (''),
        #                         'PatientFfriend': (''),
        #                         'doctor': (''),
        #                         'Jop': (''),
        #                         'Area': (''),
        #                         'PatientMobile1': (''),
        #                         'PatientMobile2': ('')
        #                     }

       
        
    # def __init__(self, *args, **kwargs):
    #     super(PatientForm, self).__init__(*args, **kwargs)
    #     if 'initial' in kwargs:
    #         self.fields['PatientPackages'].queryset = Packages.objects.filter(Active=True)                    
        
                                
class ReservationtForm(forms.ModelForm):
    class Meta:
        model = models.Reservation
        fields = "__all__"
        Widget={
            
            'FromTimeReservation': DateInput(attrs={'type': 'date'}),}
            
        
        
         
        labels = {
            'Patient': ('اسم العميل'),
            'DateReservation': (''),
            'FromTimeReservation': (''),
            'ToTimeReservation': (''),
            'Doctor': (''),
            'Branch': (''),
            'Clinc': (''),
            'Reservation': (''),
            
            
            },

        help_texts = {
                               'Patient': ('x'),
                                'DateReservation': (''),
                                'FromTimeReservation': (''),
                                'ToTimeReservation': (''),
                                'Doctor': (''),
                                'Branch': (''),
                                'Clinc': (''),
                                'Reservation': (''),
                            }
        

class PackagesForm(forms.ModelForm):  
    class Meta:
        model = models.Packages
        fields = "__all__"
        # widgets = {
        #     'PackageName': Select2Widget,
        #     'PackageParts': Select2Widget,

        # }


class RoomForm(forms.ModelForm):  
    class Meta:
        model = models.Room
        fields = "__all__"        

class AddDodtonIN(forms.ModelForm):  
    class Meta:
        model = models.DoctorIn
        fields = "__all__"                

class BranchForms(forms.ModelForm):  
    class Meta:
        model = models.Branch
        fields = "__all__"  

class AreaForm(forms.ModelForm):  
    class Meta:
        model = models.Area
        fields = "__all__"    


class ClinicForm(forms.ModelForm):  
    class Meta:
        model = models.Clinc
        fields = "__all__"  


class JobForm(forms.ModelForm):  
    class Meta:
        model = models.Jop
        fields = "__all__"                             


class DeviceForms(forms.ModelForm):  
    class Meta:
        model = models.Device
        fields = "__all__"            


class DoctorInForms(forms.ModelForm):  
    class Meta:
        model = models.DoctorIn
        fields = "__all__"     


class DoctorOutForms(forms.ModelForm):  
    class Meta:
        model = models.DoctorOut
        fields = "__all__"     


class ItemForm(forms.ModelForm):  
    class Meta:
        model = models.Item
        fields = "__all__"          







class ItemPForm(forms.ModelForm):  
    class Meta:
        model = models.Item
        fields = [ 'title','price','CountBalces', 'BalcesNumber','PackageParts','description_short','image']
    

class ItemSForm(forms.ModelForm):  
    class Meta:
        model = models.Item
        fields = [ 'title','price','description_short','image']    



         

class OrderDiscount(forms.ModelForm):  
    class Meta:
        model = models.Order
        fields = [ 'Discount','ordered']    
           

class OrderPayment(forms.ModelForm):  
    class Meta:
        model = models.Order
        fields = [ 'Cash',]  


class BallsTransaction(forms.ModelForm):  
    class Meta:
        model = models.Transaction
        fields = "__all__"         
             
                      
class OrderPayment(forms.ModelForm):  
    class Meta:
        model = models.Order
        fields = [ 'Cash']                        