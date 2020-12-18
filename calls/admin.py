from django.contrib import admin


from .models import  calls , statue
from import_export.admin import ImportExportModelAdmin 

admin.site.register(calls)
admin.site.register(statue)