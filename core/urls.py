# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    #path('admin' , admin.site.urls),          # Django admin route 
    path("", include("authentication.urls")), # Auth routes - login / register
    path("", include("app.urls"))  ,           # UI Kits Html files
    path("", include("testapp.urls")),
    path("", include("novav1.urls")),
    path("", include("event_manage.urls")),
    path("", include("calls.urls")),
    path("select2/", include("django_select2.urls")),
]
