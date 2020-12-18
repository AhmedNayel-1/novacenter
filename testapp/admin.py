from django.contrib import admin

# Register your models here.
from .models import names 
from .models import Entry, Language ,Events

admin.site.register(Entry)
admin.site.register(Language)
admin.site.register(Events)
admin.site.register(names)
