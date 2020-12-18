

from django.contrib import admin
from django.urls import  path
from django.conf.urls import url
from . import views
app_name = 'event_manage'

urlpatterns = [                          
   path('event/', views.event, name="manage-event"),
   url('^calendareve', views.calendar, name='calendar'),
   url('^add_event$', views.add_event, name='add_event'),
   url('^update$', views.update, name='update'),
   url('^remove', views.remove, name='remove'),
    url('^add_event$', views.add_event, name='add_event_to_end'),

    #path('crud/', views.CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/create/', views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/delete/', views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/update/', views.UpdateCrudUser.as_view(), name='crud_ajax_update'),

    path('newevent', views.newevent, name='newevent'),

    path('eventreservation/<int:id>', views.update, name='eventreservation'),

    path("eventcreate", views.EventCreateView, name="Event-create"), 
    path("eventcreatenew", views.EventCreateView_new, name="Event-create-new"), 
    path("arrive", views.ArriveCreateView.as_view(), name="Arrive-create"), 
    path("session/<int:id>", views.sessionDetail, name="Session-create"), 
    
    
    path("reception", views.reception_all_reserv, name="reception_all_reserv"), 
    path("reception/arrive", views.reception_reserv_arrive, name="reception_reserv_arrive"), 
    path("reception/srart", views.reception_reserv_srart, name="reception_reserv_srart"), 
    path("balls_entry/<int:event_id>/", views.balls_entry, name="balls_entry"),

    path("onofarrive/<int:id>/", views.onofarrive, name="onofarrive"), 
    path("onofstart/<int:id>/", views.onofarrive, name="onofstart"), 

    
    path('eventtype/<int:id>/', views.make_call_for_events, name='make_call_for_events'),               
    

    path('eventfilter/',views.filter,name="eventfilter"),        

    path('calendertest/',views.calendertest,name="calendertest"), 

     

    path('prametars/<int:id>/',views.dvice_prametars,name="prametars"),
    path("prametarsentry/<int:id>/", views.paramentry, name="prametars_entry"),


    path("prametersreport/<int:id>/", views.prametersreport, name="prametersreport"),

    path("eventparameters/<int:part_id>/<int:id>/", views.allInOneView, name="allInOneView"),


]
