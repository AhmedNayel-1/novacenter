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


class callsForms(forms.ModelForm):  
    class Meta:
        model = models.calls
        fields = ['Note','Statue','Followup']    

        labels = {
            'Note': (''),
            'Statue': (''),
            'Followup': (''),
            
            
            
            }
