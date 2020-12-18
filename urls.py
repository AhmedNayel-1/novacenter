from django.contrib import admin
from django.urls import  path

from . import views

urlpatterns = [
    path("newPatient", views.PatientCreateView.as_view(), name="Patient-create"),
    path("newreservation", views.ReservationCreateView.as_view(), name="Reservation-create"),
    path("datareservation", views.ReservationData.as_view(), name="Reservation-data"),
    path("PackagesCreate", views.PackagesCreateView.as_view(), name="Packages-create"),
    path('Patientsearch/',views.Search,name="Patient-search"),
    path("roomCreate", views.RoomCreateView.as_view(), name="room-create"),
    path("area", views.AreaCreateView.as_view(), name="area-create"),
    path("Branch", views.BranchCreateView.as_view(), name="branch-create"), 
    path("Device", views.DeviceCreateView.as_view(), name="Device-create"), 
    path("DoctorIn", views.DoctorInCreateView.as_view(), name="DoctorIn-create"), 
    path("DoctorOut", views.DoctorOutCreateView.as_view(), name="DoctorOut-create"), 
 
    path("adddoctor", views.AddDodtonIN.as_view(), name="add-doctor"),
    path('PackagesCreate/<int:id>/', views.onofPatient, name='onof-Patient'),
    path('area/<int:id>/', views.onofArea, name='onof-Area'),
    path('Branch/<int:id>/', views.onofBranch, name='onof-Branch'),
    path('Device/<int:id>/', views.onofDevice, name='onof-Device'),
    path('DoctorIn/<int:id>/', views.onofDoctorIn, name='onof-DoctorIn'),
    path('DoctorOut/<int:id>/', views.onofDoctorOut, name='onof-DoctorOut'),   
    #path('toggle/', views.toggle),
    path('<int:id>/', views.onofPackages, name='onofPackages'),
    path('Patientdetail/<int:id>/', views.PatientDetailView, name='Patient-detail'),
    path('', views.index, name='index'),
]