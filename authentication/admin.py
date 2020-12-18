# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.contrib import admin


from .models import  User ,Section
from import_export.admin import ImportExportModelAdmin 

admin.site.register(User)
admin.site.register(Section)
