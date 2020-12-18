from django import forms

from django_select2 import forms as s2forms

from . import models
from novav1.models import Packages ,Patient
from django.forms import ModelChoiceField
from django.forms.widgets import *
from crispy_forms.layout import *
from crispy_forms.helper import *
from django.template import Template, Context
from django.forms.widgets import DateInput, TextInput ,DateTimeBaseInput ,TimeInput

from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget





class EventForm(forms.ModelForm):  

    
    class Meta:
        model = models.Events
        fields = ['event_name','start_date','end_date']  

    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        self.fields['event_name'] =  ModelChoiceField(queryset=Patient.objects.all())
                                            

class ArriveForm(forms.ModelForm):  
    class Meta:
        model = models.Events
        fields = ['arrive'] 



class SessionDetail(forms.ModelForm):  
    class Meta:
        model = models.Events
        fields = ['start','start_date','session_end','session_clinic','session_doctor','session_area','session_used_balls','session_branch','end','session_area']     

        labels = {
            'start_date': (''),
            'session_end': (''),
            'session_clinic': (''),
            'session_doctor': (''),
            'session_area': (''),
            'session_used_balls': (''),
            'session_branch': (''),
            
            
            },



class callsFormsEvents(forms.ModelForm):  
    class Meta:
        model =  models.Events
        fields = ['event_type','event_note']    

        labels = {
            'event_name': (''),
            'start_date': (''),
            'end_date': (''),
            'event_type': (''),
            'event_note': (''),
            
            
            
            }


class ParametersForms(forms.ModelForm):  
    class Meta:
        model =  models.deviceparameters
        fields =['Joule','msec','PulseCount','OperatorName']    

                 