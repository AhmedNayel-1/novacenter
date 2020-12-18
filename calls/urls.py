from django.contrib import admin
from django.urls import path, include  # add this
from . import views

app_name = 'calls'
urlpatterns = [

    path('customers_list',views.customers_list,name='call_list'),
    path('follow_up_calls_today',views.Follow_up_calls_today,name='Follow_up_calls'),
    path('follow_up_calls_all',views.Follow_up_calls_all,name='Follow_up_calls_all'),
    path('call/<int:id>/', views.make_call, name='make_call'),


]