from django import forms
from .models import Entry, Language, names


class EntryCreationForm(forms.ModelForm):

    class Meta:
        model = Entry
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['language'].queryset = Language.objects.none()
        self.fields['name'].queryset = names.objects.none()

        if 'language' in self.data:
            self.fields['language'].queryset = Language.objects.all()
        if 'name' in self.data:
            self.fields['language'].queryset = names.objects.all()
        elif self.instance.pk:
            self.fields['language'].queryset = Language.objects.all().filter(pk=self.instance.language.pk)
        
            self.fields['name'].queryset = names.objects.all().filter(pk=self.instance.name.pk)     
             
