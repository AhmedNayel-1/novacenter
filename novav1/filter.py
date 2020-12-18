import django_filters
from .models import Patient
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.layout import (Layout, Fieldset, Field,
                                 ButtonHolder, Submit, Div)

class PatientFilter(django_filters.FilterSet):
    PatientName = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Patient
        #fields = '__all__'
        fields = ['PatientName']
        labels = {
           'PatientName':'Address Description',
            
            }

          

    def __init__(self, *args, **kwargs):
        super(PatientFilter, self).__init__(*args, **kwargs)
        # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
        if self.data == {}:
            self.queryset = self.queryset.none()
            self.filters['PatientName'].label="برجاء ادخال السريال المدون بكارت الضمان"
            self.helper = FormHelper()
            self.helper.form_class = 'form-control form-control-lg'
            #self.helper.label_class = 'input-group input-group-lg'
            self.helper.field_class = 'form-control form-control-lg'
            self.helper.layout = Layout(
                                     Field('PatientName', placeholder='Search ...'),
        )


# helper.form_class = 'form-horizontal'
# helper.label_class = 'col-lg-2'
# helper.field_class = 'col-lg-8'
# helper.layout = Layout(
#     'email',
#     'password',
#     'remember_me',
#     StrictButton('Sign in', css_class='btn-default'),
# )



# full_search = django_filters.CharFilter(method='search_by_full_search', label='Recherche') # change label field to reflect what the filter name should be

# class Meta:
#    model = myModel
#    fields = ['full_search', ]

# def search_by_full_search(self, qs, name, value):
#     for term in value.split():
#       qs = qs.filter(Q(serial__icontains=term) | Q(id__icontains=term) | 
#       Q(name__icontains=term))
#     return qs            
