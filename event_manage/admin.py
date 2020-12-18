from django.contrib import admin

# Register your models here.
from .models import Events ,CrudUser ,EventType ,deviceparameters,Event
from import_export.admin import ImportExportModelAdmin 



# @admin.register()
# class EventAdmin(ImportExportModelAdmin):
#      pass

admin.site.register(Events)
admin.site.register(EventType)
admin.site.register(deviceparameters)
admin.site.register(Event)