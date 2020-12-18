from django.contrib import admin

# Register your models here.
from .models import DoctorOut,DoctorIn ,Area,Clinc,Comefrom,Gender,Jop,Patient,Reservation,Stractuer,Branch,Device,Room,pricing,Packages,Item,Category,Order,OrderItem,Coupon,Refund,Transaction,ballses,Order_type
from import_export.admin import ImportExportModelAdmin                     

admin.site.register(Reservation)
admin.site.register(Area)
admin.site.register(Clinc)
admin.site.register(Comefrom)
admin.site.register(Gender)
admin.site.register(Jop)
#admin.site.register(Patient)
admin.site.register(DoctorIn)
admin.site.register(DoctorOut)
admin.site.register(Stractuer)
#admin.site.register(Reservation)
admin.site.register(Branch)
admin.site.register(Device)
admin.site.register(Room)
admin.site.register(pricing)
admin.site.register(Packages)
admin.site.register(Item)
admin.site.register(Category)  
admin.site.register(ballses) 
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Coupon)
admin.site.register(Refund)  
admin.site.register(Transaction)
admin.site.register(Order_type)
@admin.register(Patient)
class PatientAdmin(ImportExportModelAdmin):  
     pass