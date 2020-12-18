from django.contrib import admin
from django.urls import  path

from . import views

# urlpatterns = [
#     path("newPatient", views.PatientCreateView.as_view(), name="Patient-create"),
#     path("newreservation", views.ReservationCreateView.as_view(), name="Reservation-create"),
#     path("datareservation", views.ReservationData.as_view(), name="Reservation-data"),
#     path("PackagesCreate", views.PackagesCreateView.as_view(), name="Packages-create"),
#     path('Patientsearch/',views.Search,name="Patient-search"),
#     path("roomCreate", views.RoomCreateView.as_view(), name="room-create"),
#     path("adddoctor", views.AddDodtonIN.as_view(), name="add-doctor"),
#     path('PackagesCreate/<int:id>/', views.onofPatient, name='onof-Patient'),
#     path('areaCreate/<int:id>/', views.onofArea, name='onof-area'),
#     #path('toggle/', views.toggle),
#     path('<int:id>/', views.onofPackages, name='onofPackages'),
#     path('Patientdetail/<int:id>/', views.PatientDetailView, name='Patient-detail'),
#     path('', views.index, name='index'),
#     path("area", views. AreaCreateView.as_view(), name="area-create"),
#     path("clinic", views. ClinicCreateView.as_view(), name="clinic-create"),
#     path('clinic/<int:id>/', views.onofclinic, name='onof-clinic'),
#     path("job", views.JopCreateView.as_view(), name="job-create"),
#     path('job/<int:id>/', views.onofjob, name='onof-job'),


# ]

urlpatterns = [
    path("newPatient", views.PatientCreateView.as_view(), name="Patient-create"),
    path("newreservation", views.ReservationCreateView.as_view(), name="Reservation-create"),
    path("datareservation", views.ReservationData.as_view(), name="Reservation-data"),
    path("PackagesCreate", views.PackagesCreateView.as_view(), name="Packages-create"),
    #path('Patientsearch/',views.Search,name="Patient-search"),
    path("roomCreate", views.RoomCreateView.as_view(), name="room-create"),
    path("area", views.AreaCreateView.as_view(), name="area-create"),
    
    # path("Device", views.DeviceCreateView.as_view(), name="Device-create"), 
    # path("DoctorIn", views.DoctorInCreateView.as_view(), name="DoctorIn-create"), 
    # path("DoctorOut", views.DoctorOutCreateView.as_view(), name="DoctorOut-create"), 
    path("area", views.AreaCreateView.as_view(), name="area-create"),
    
    path("Device", views.DeviceCreateView.as_view(), name="Device-create"), 
    path("DoctorIn", views.DoctorInCreateView.as_view(), name="DoctorIn-create"), 
    path("DoctorOut", views.DoctorOutCreateView.as_view(), name="DoctorOut-create"), 
    path('Branch/<int:id>/', views.onofBranch, name='onof-Branch'),
    path('Device/<int:id>/', views.onofDevice, name='onof-Device'),
     
    path("Branch", views.BranchCreateView.as_view(), name="branch-create"), 


    # path("adddoctor", views.AddDodtonIN.as_view(), name="add-doctor"),
    path('PackagesCreate/<int:id>/', views.onofPatient, name='onof-Patient'),
    path('area/<int:id>/', views.onofArea, name='onof-area'),
    path('Branch/<int:id>/', views.onofBranch, name='onof-Branch'),
    path('Device/<int:id>/', views.onofDevice, name='onof-Device'),
    path('DoctorIn/<int:id>/', views.onofDoctorIn, name='onof-DoctorIn'),
    path('DoctorOut/<int:id>/', views.onofDoctorOut, name='onof-DoctorOut'),   
    #path('toggle/', views.toggle),
    path('onofPackages/<int:id>/', views.onofPackages, name='onofPackages'),
    path('Patientdetail/<int:id>/', views.PatientDetailView, name='Patient-detail'),

    path("clinic", views. ClinicCreateView.as_view(), name="clinic-create"),
    path('clinic/<int:id>/', views.onofclinic, name='onof-clinic'),

    path("item", views. ItemCreateView.as_view(), name="item-create"),
    path('item/<int:id>/', views.onofitem, name='onof-item'),
 
    path("itemP", views. ItemPCreateView.as_view(), name="itemP-create"),
    path('itemP/<int:id>/', views.onofitem, name='onof-itemP'),

    path("itemS", views. ItemSCreateView.as_view(), name="itemS-create"),
    path('itemS/<int:id>/', views.onofitem, name='onof-itemS'),

    path("itemslist/<int:pid>/", views.itemslist, name="items-list"),
     path("itemslist2/<int:pid>/", views.itemslist2, name="items-list2"),

    path('add-to-cart/<int:id>/<int:pid>/', views.add_to_cart, name='add-to-cart'),   
    
    path('remove-item-from-cart/<int:id>/<int:pid>/', views.remove_single_item_from_cart,
         name='remove-single-item-from-cart'),

    path('remove-from-cart/<int:id>/<int:pid>/', views.remove_from_cart, name='remove-from-cart'),

    #path('search/', views.SearchResultsView.as_view(), name='search_results'), 
    path('search/', views.search, name='search'), 
    
   # path('', views.index, name='index'),

    path('edit/<int:pid>/', views.edit, name='edit'),
    path('payment/<int:pid>/', views.payment, name='payment'),      
    # path('edit_paper/<int:pk>', views.load_paper, name='edit_paper'),   
    # path('checkout/', views.CheckoutView.as_view(), name='checkout'),
    # path('add_coupon/', views.AddCouponView.as_view(), name='add-coupon'),
    # path('payment/<payment_option>/', views.PaymentView.as_view(), name='payment'),
    # path('request-refund/', views.RequestRefundView.as_view(), name='request-refund'),
    #path('calenderCreateView/', views.calenderCreateView.as_view(), name="calenderCreateView"),

    path('balls_transaction', views.balls_transaction, name='balls_transaction'),
    path('payments', views.just_payment, name='just_payment'),
    path('refund', views.Refunds, name='refund'),


    path('cashbalance/<int:pid>/', views.cashbalance, name='cashbalance'),
    path('ballsbalance/<int:pid>/', views.ballsbalance, name='ballsbalance'),

    path('reserv', views.reserv, name='reserv'),# for test
    
]
