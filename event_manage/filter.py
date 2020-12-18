import django_filters
from .models import Events
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit,Field
from bootstrap_datepicker_plus import DatePickerInput

class EventsFilter(django_filters.FilterSet):
    #name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Events
        # fields = '__all__'
        fields = ['start_date','event_type','event_doctor','end_date','branch_event','event_service','event_clinic']
        labels = {
            'start_date': (''),
            'event_type': (''),
            'event_doctor': (''),
            'end_date': (''),
            'branch_event': (''),
            'event_service': (''),
            'event_clinic': ('')
        }
        
        widgets = {
        'start_date': DatePickerInput(),
        }
        
          

    # def __init__(self, *args, **kwargs):
    #     super(Events, self).__init__(*args, **kwargs)
    #     # at sturtup user doen't push Submit button, and QueryDict (in data) is empty
    #     if self.data == {}:
    #         self.queryset = self.queryset.none()
    #         self.filters['Sireal'].label="برجاء ادخال السريال المدون بكارت الضمان"
    #         self.helper = FormHelper()
    #         self.helper.layout = Layout(
    #         Field('Sireal', placeholder='Search ...'),
    #     )