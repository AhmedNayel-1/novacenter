from django.contrib import admin
from django.urls import path, include  # add this
from .views import TestNames , home ,calendar ,add_event , update ,remove

urlpatterns = [
    path('data', TestNames, name="data"),
    path('select2', home, name="select2"),
    #path('calendar', calendar, name='calendar'),



    path('calendar', calendar, name='calendar'),
    path('add_event', add_event, name='add_event'),
    path('update', update, name='update'),
    path('remove', remove, name='remove'),

]  