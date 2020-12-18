from django.shortcuts import render ,redirect ,get_object_or_404 

# Create your views here.

from django.views import generic
from . import forms, models
from .filter import PatientFilter
from django.utils import timezone
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist , MultipleObjectsReturned
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.db.models import Q 
from django.db.models import Sum
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import random
import string
import math
from itertools import zip_longest 
from calls.models import calls
from calls.models import calls
from event_manage.models import Events
from event_manage.models import Events
from datetime import datetime ,date
def create_ref_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

class PatientCreateView(generic.CreateView):
    template_name="core/templates/Patient_form.html"
    model = models.Patient
    form_class = forms.PatientForm
    success_url = "/"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context


class ReservationCreateView(generic.CreateView):
    template_name="core/templates/reservation.html"
    model = models.Reservation
    form_class = forms.ReservationtForm
    success_url = "/"    



class ReservationData(generic.ListView):
        template_name="core/templates/reservation_data.html"
        model = models.Reservation
        





class PackagesCreateView(generic.CreateView):
    template_name="core/templates/Packages.html"
    model=models.Packages
    form_class=forms.PackagesForm
    success_url= "/PackagesCreate"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context


# def Search(request): 
#     filter = PatientFilter(request.GET, queryset=models.Patient.objects.all())
#     Patients= models.Patient.objects.all()
   
    
#     context={
#                'Patients':Patients,
#                'filter': filter
#     }
#     return render(request, 'Search.html', context)



class RoomCreateView(generic.CreateView):
    template_name="core/templates/room.html"
    model=models.Room
    form_class=forms.RoomForm
    success_url= "/roomCreate"    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context



# class AddDodtonIN(generic.CreateView):
#     template_name="core/templates/doctorin.html"
#     model=models.DoctorIn
#     form_class=forms.AddDodtonIN
#     success_url= "/DoctorInCreate"    

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["objects"] = self.model.objects.all()
#         return context        





def onofPatient(requset,id):
    a = get_object_or_404(models.Patient, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("Patient-create")
    
    #return HttpResponseRedirect(reverse('t_attendance_detail', args=(a.student.USN, a.course_id)))

def onofPackages(requset,id):
    b = get_object_or_404(models.Packages, pk=id)
    b.Active = not b.Active
    print(b)
    b.save()
    return redirect("/PackagesCreate")          

def onofArea(requset,id):
    a = get_object_or_404(models.Area, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("area-create")
    




def PatientDetailView(requset,id):
    Patients   = models.Patient
    Reservation= models.Reservation
    order      = models.Order
    ballsestrans    = models.Transaction
    Patientdata  =   models.Patient.objects.get(id=id)
    

    PatientDetail    =Patients.objects.filter(id=id)
    ReservationDetail= Reservation.objects.filter(Patient_id=id)
    totalReservation = Reservation.objects.filter(Patient_id=id).count()

    Pyments          = order.objects.filter(Patient_id=id ,order_type=4)
    #sales            = get_object_or_404(order, Patient_id=id ,order_type=1)
    sales            = models.OrderItem .objects.filter(Patient_id=id )
    # sales            = order.objects.filter(Patient_id=id ,order_type=1)
    Refunds          = order.objects.filter(Patient_id=id ,order_type=5)
    callshistory     = calls.objects.filter(Customer_id=id )
    balls_transaction= ballsestrans.objects.filter(Q(from_user=id) | Q(to_user=id) )

    #totalCansel = Invoice.objects.filter(stut_order_id=2).count()
     
    context={
        'PatientDetail':PatientDetail,
        'totalReservation':totalReservation,
        'ReservationDetail':ReservationDetail,
        'Pyments':Pyments,
        'Patientdata':Patientdata,
        'sales':sales,
        'Refunds':Refunds,
        'callshistory':callshistory,
        'balls_transaction':balls_transaction,
    }

    return render(requset,'core/templates/Patient-detail.html',context)
      





class AreaCreateView(generic.CreateView):
    template_name="core/templates/area_form.html"
    model = models.Area
    form_class = forms.AreaForm
    success_url = "/area"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context       


class ClinicCreateView(generic.CreateView):
    template_name="core/templates/Clinic_form.html"
    model = models.Clinc
    form_class = forms.ClinicForm
    success_url = "/clinic"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context  

def onofclinic(requset,id):
    a = get_object_or_404(models.Clinc, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("clinic-create")

class JopCreateView(generic.CreateView):
    template_name="core/templates/Jop_form.html"
    model = models.Jop
    form_class = forms.JobForm
    success_url = "/job"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context  

def onofjob(requset,id):
    a = get_object_or_404(models.Jop, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("/job")
    
class BranchCreateView(generic.CreateView):
    template_name="core/templates/Branch_form.html"
    model = models.Branch
    form_class = forms.BranchForms
    success_url = "/Branch"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context 


class DeviceCreateView(generic.CreateView):
    template_name="core/templates/Device_form.html"
    model = models.Device
    form_class = forms.DeviceForms
    success_url = "/Device"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context        
        
class DoctorInCreateView(generic.CreateView):
    template_name="core/templates/DoctorIn_form.html"
    model = models.DoctorIn
    form_class = forms.DoctorInForms
    success_url = "/DoctorIn"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context        


class DoctorOutCreateView(generic.CreateView):
    template_name="core/templates/DoctorOut_form.html"
    model = models.DoctorOut
    form_class = forms.DoctorOutForms
    success_url = "/DoctorOut"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context       



def onofBranch(requset,id):
    a = get_object_or_404(models.Branch, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("branch-create")
        
def onofDevice(requset,id):
    a = get_object_or_404(models.Device, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("Device-create")        


def onofDoctorIn(requset,id):
    a = get_object_or_404(models.DoctorIn, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("DoctorIn-create")

def onofDoctorOut(requset,id):
    a = get_object_or_404(models.DoctorOut, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("DoctorOut-create")



class ItemCreateView(generic.CreateView):
    template_name="core/templates/Item_form.html"
    model = models.Item
    form_class = forms.ItemForm
    success_url = "/item"
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.all()
        return context  

def onofitemP(requset,id):
    a = get_object_or_404(models.Item, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("item-create")    




class ItemPCreateView(generic.CreateView):
    template_name="core/templates/ItemP_form.html"
    model = models.Item
    form_class = forms.ItemPForm
    success_url = "/itemP"
    

    def form_valid(self, form):
        Category=models.Category
        c= Category.objects.get(id=1)
        form.instance.category = c
        return super(ItemPCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.filter(category=1)
        return context  


def onofitemS(requset,id):
    a = get_object_or_404(models.Item, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("itemP-create")    


class calenderCreateView(generic.CreateView):
    template_name="core/templates/calendar.html"
    model = models.Item
    form_class = forms.ItemSForm
    success_url = "/itemS"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.filter(category=2)
        return context  

class ItemSCreateView(generic.CreateView):
    template_name="core/templates/ItemS_form.html"
    model = models.Item
    form_class = forms.ItemSForm
    success_url = "/itemS"
    

    def form_valid(self, form):
        Category=models.Category
        c= Category.objects.get(id=2)
        form.instance.category = c
        return super(ItemSCreateView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["objects"] = self.model.objects.filter(category=2)
        return context  

def onofitem(requset,id):
    a = get_object_or_404(models.Item, id=id)
    a.Active = not a.Active
    a.save()
    return redirect("itemS-create")  



# @login_required
# def createpost(request):
#         if request.method == 'POST':
#             if request.POST.get('title') and request.POST.get('content'):
#                 post=Post()
#                 post.title= request.POST.get('title')
#                 post.content= request.POST.get('content')
#                 post.author= request.user
#                 post.save()
	
# 		messages.success(request, "Your post has been successfully created")
                

#                 return render(request, 'posts/create.html')  

       
#          else:
# 	     context= {'error': 'The post was not successfully created. Please enter a title and content'}
#              return render(request,'posts/create.html', context)



def itemslist(request,pid):
    try:
            cat1     =   models.Item.objects.filter(category=1)
            cat2     =   models.Item.objects.filter(category=2)
            order    =   models.OrderItem.objects.get(ordered=False,Patient=pid)
            #order    =   get_object_or_404(models.Order, ordered=False,Patient=pid)
            Patientdata  =   models.Patient.objects.get(id=pid)
                
            context={
                'cat1':cat1,
                'cat2':cat2,
                'object': order,
                'Patientdata': Patientdata

            }
            
            return render(request,"core/templates/shop.html",context)
    except ObjectDoesNotExist:
            cat1     =   models.Item.objects.filter(category=1)
            cat2     =   models.Item.objects.filter(category=2)
            #order    =   models.Order.objects.get(ordered=False,Patient=14)
            Patientdata  =   models.Patient.objects.get(id=pid)
            context={
                'cat1':cat1,
                'cat2':cat2,
                #'object': order,
                'Patientdata': Patientdata

            }
              
            messages.error(request, "You do not have an active order")
            return render(request,"core/templates/shop.html",context)   











def add_to_cart(request, id , pid ):
    item = get_object_or_404(models.Item, id=id)
    Patient=get_object_or_404(models.Patient, id=pid)
    
    #price=item.price
    
    order_item, created = models.OrderItem.objects.get_or_create(
        item=item,
        Patient=Patient,
        user=request.user,
        ordered=False,
        #price=price
        
    )

    
   
    invoce=models.OrderItem.objects.filter(Patient=pid)
    coupon=models.Coupon.objects.all
    totalBallce = 0
    for p in invoce:
            totalBallce += p.item.CountBalces *p.quantity
    # if coupon:
    #     total -= coupon.amount
    totalamount = 0
    for p in invoce:
            totalamount += p.item.price *p.quantity         
    
    # Patient.AmountBalance=totalamount
    # Patient.BallceBalance=totalBallce
    # Patient.save()
    obj = models.ballses.objects.create(
            Patient = Patient,
            
            #user = request.user,
            transaction_type= 4,
            ballses_count= totalBallce

        )



    order_qs = models.Order.objects.filter(Patient=Patient, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__id=item.id).exists():
            order_item.quantity += 1
            order_item.save()
            # totalBallce = 0
            # for p in invoce:
            #         totalBallce += p.item.CountBalces * (p.quantity+1)
            # # if coupon:
            # #     total -= coupon.amount
            # totalamount = 0
            # for p in invoce:
            #         totalamount += p.item.price * p.quantity 
            # Patient.AmountBalance=totalamount
            # Patient.BallceBalance=totalBallce 
            
            # Patient.save()


        #     obj = models.ballses.objects.update(
        #     Patient = Patient,
            
        #     #user = request.user,
        #     transaction_type= 4,
        #     ballses_count= invoce.item.CountBalces

        # )

            messages.info(request, "Item qty was updated.")
            return redirect('items-list2', pid=pid)
        else:
            order.items.add(order_item)
            messages.info(request, "Item was added to your cart.")
            print(order_item)
            return redirect('items-list2', pid=pid)
    else:
        ordered_date = timezone.now()
        order = models.Order.objects.create( Patient=Patient,
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        print(order_item.price)
        messages.info(request, "Item was added to your cart.")
    return redirect('items-list2', pid=pid)    


   




def remove_single_item_from_cart(request, id, pid):
    item = get_object_or_404(models.Item, id=id)
    Patient=get_object_or_404(models.Patient, id=pid)
    order_qs = models.Order.objects.filter(
        Patient=Patient,
        user=request.user,
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = models.OrderItem.objects.filter(
                Patient=Patient,
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            messages.info(request, "This item qty was updated.")
            return redirect('items-list2', pid=pid)
        else:
            # add a message saying the user dosent have an order
            messages.info(request, "Item was not in your cart.")
            return redirect('items-list2', pid=pid)
    else:
        # add a message saying the user dosent have an order
        messages.info(request, "u don't have an active order.")
        return redirect('items-list2', pid=pid)
    return redirect('items-list2', pid=pid)








def remove_from_cart(request, id,pid):
    url = request.META.get('HTTP_REFERER') 
    item = get_object_or_404(models.Item, id=id)
    Patient=get_object_or_404(models.Patient, id=pid)
    order_qs = models.Order.objects.filter(
        Patient=Patient,
        user=request.user,
        ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__id=item.id).exists():
            order_item = models.OrderItem.objects.filter(
                Patient=Patient,
                item=item,
                user=request.user,
                ordered=False
                
            )[0]
            order.items.remove(order_item)
            messages.info(request, "تم الحذف")
            #return redirect("core:category")
            return HttpResponseRedirect(url)
        else:
            # add a message saying the user dosent have an order
            messages.info(request, "الخدمه ليست موجوده")
            #return redirect("core:category", slug=slug)
            return HttpResponseRedirect(url)
    else:
        # add a message saying the user dosent have an order
        messages.info(request, "لايوجد طلبات حاليه")
        #return redirect("core:category", slug=slug)
        return HttpResponseRedirect(url)
    return redirect('items-list', pid=pid)  

from django.core import serializers
###############################################################
def itemslist2(request,pid):
    url = request.META.get('HTTP_REFERER') 
    try:
            cat1     =   models.Item.objects.filter(category=1)
            cat2     =   models.Item.objects.filter(category=2)
            order    =   models.Order.objects.get(ordered=False,Patient=pid)
            #order        =   get_object_or_404(models.Order, ordered=False,Patient=pid)
            cat_all     =   models.Item.objects.all()
            #editdata = models.Order.objects.get(Patient=pid) 
            Patientdata  =   models.Patient.objects.get(id=pid)
            orderitems=  models.Order.items
            
            form = forms.OrderDiscount(request.POST, instance=order)
            if request.method == 'POST':
                form = forms.OrderDiscount(request.POST, instance=order)
                if form.is_valid():
                   form.save()
                   return redirect('payment', pid=pid)
            else:       
                    context={
                        'cat1':cat1,
                        'cat2':cat2,
                        'object': order,
                        'form':form,
                        'Patientdata': Patientdata,
                        'cat_all':cat_all

                    }
                    print(orderitems)
                    return render(request,"core/templates/shop2.html",context)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
            cat1     =   models.Item.objects.filter(category=1)
            cat2     =   models.Item.objects.filter(category=2)
            #order    =   models.Order.objects.get(ordered=False,Patient=pid)
            Patientdata  =   models.Patient.objects.get(id=pid)
            cat_all     =   models.Item.objects.all()
            context={
                'cat1':cat1,
                'cat2':cat2,
                'cat_all':cat_all,
                'Patientdata': Patientdata

            }
              
            messages.error(request, "You do not have an active order")
            return render(request,"core/templates/shop2.html",context) 



    





def search(request):
    Patients= models.Patient.objects.all
    if request.method == 'GET':
        query= request.GET.get('q')
      
        submitbutton= request.GET.get('submit')

        if query is not None:
            lookups= Q(PatientName__icontains=query) | Q(PatientMobile1__icontains=query)

            results= models.Patient.objects.filter(lookups).distinct()

            context={'results': results,
                     'submitbutton': submitbutton,
                     'Patients':Patients
                     }

            return render(request, 'core/templates/search.html', context)

        else:
            return render(request, 'core/templates/search.html',{'Patients':Patients})

    else:
        return render(request, 'core/templates/search.html',{'Patients':Patients})



# DISCOUNT - CACHE- PID- TOTAL_Price
def edit(request, pid ):
    order = models.Order.objects.get(ordered=False,Patient=pid)
    #editdata = models.Order.objects.get(Patient=pid)
    Patientdata  =   models.Patient.objects.get(id=pid) 
    if request.method == 'POST':
        form = forms.OrderDiscount(request.POST, instance=order)
        if form.is_valid():
           form.save()
           return redirect("payment", pid=pid)
           #return redirect('items-list2', pid=pid)
    else:
        form = forms.OrderDiscount(instance=order)
    return render(request, 'core/templates/form.html', {'form':form,'order': order,'Patientdata': Patientdata}) 




def payment(request, pid ):
    order = models.Order.objects.get(ordered=False,Patient=pid)
    ordertotals = models.Order.objects.filter(ordered=False,Patient=pid)
    
    #editdata = models.Order.objects.get(Patient=pid)
    Patientdata  =   models.Patient.objects.get(id=pid) 
    if request.method == 'POST':
        form = forms.OrderPayment(request.POST, instance=order)
        if form.is_valid():
           newform = form.save(commit=False)
           newform.ref_code = create_ref_code()
           newform.ordered = True
           ordered_date =  datetime.now()
           newform.save()
           order_qs = models.OrderItem.objects.filter(Patient=pid, ordered=False) #models.OrderItem.objects.filter(Patient=pid, ordered=False)
           if order_qs.exists():
                order = order_qs[0]
                order.ordered  = not order_qs.ordered
                
                order.save()

            
           return redirect("/")
           #return redirect('items-list2', pid=pid)
    else:
        form = forms.OrderPayment(instance=order)
    return render(request, 'core/templates/form_pay.html', {'form':form,'order': order,'ordertotals': ordertotals,'Patientdata': Patientdata}) 


# @login_required
# def destroy(request, id_invoice):
#     orders = Invoice.objects.get(id_invoice=id_invoice)
#     orders.delete()
#     return redirect('/', messages.success(request, 'Order was successfully deleted.', 'alert-success'))


# def load_paper(request):
#     pk = request.GET.get('pk')
#     object = models.Order.objects.get(Paper, pk = pk)
#     form = forms.OrderPayment(instance=object)
#     return render(request, 'core/templates/shop2.html', {
#         'object': object,
#         'pk': pk,
#         'form': form,
#         })



def balls_transaction(request):
    person       = models.Patient.objects.all()
    Transactions  = models.Transaction.objects.all()
    if request.method=='POST':
        from_user = models.Patient.objects.get(pk=int(request.POST.get('f')))
        to_user = models.Patient.objects.get(pk=int(request.POST.get('t')))
        amount = request.POST['amount']
        user = request.user

        obj = models.Transaction.objects.create(
            from_user = from_user,
            to_user = to_user,
            amount = amount,
        )

        objtoadd = models.Order.objects.create(
            Patient_from = from_user,
            Patient = to_user,
            balls = amount,
            order_type= "2",
            ordered_date= datetime.now(),
            user = user
        )
        objtodelet = models.Order.objects.create(
            Patient = from_user,
            Patient_from = to_user,
            balls = amount,
            order_type= "3",
            ordered_date= datetime.now(),
            user = user
        )

       
        return redirect ('/')
    return render(request, 'core/templates/transactions.html',{'person':person ,'Transactions':Transactions}) 



def just_payment(request):
    person       = models.Patient.objects.all()
    orders  = models.Order.objects.all()

    if request.method=='POST':
        Patient = models.Patient.objects.get(pk=int(request.POST.get('Patient')))
        #Cash = models.Patient.objects.get(pk=int(request.POST.get('cash')))
        Cash = request.POST['Cash']
        user = request.user
        pid  =   request.POST['Patient']


        obj = models.Order.objects.create(
            Patient = Patient,
            Cash = Cash,
            user = user,
            ordered_date = datetime.now(),
            order_type= "4"

        )

        
        return redirect ('cashbalance',pid=pid)
    return render(request, 'core/templates/payments.html',{'person':person ,'orders':orders}) 



def Refunds(request):
    person       = models.Patient.objects.all()
    orders  = models.Order.objects.all()

    if request.method=='POST':
        Patient = models.Patient.objects.get(pk=int(request.POST.get('Patient')))
        #Cash = models.Patient.objects.get(pk=int(request.POST.get('cash')))
        Cash = request.POST['Cash']
        user = request.user

        obj = models.Order.objects.create(
            Patient = Patient,
            Cash = Cash,
            user = user,
            ordered_date = datetime.now(),
            order_type= "5"

        )

        
        return redirect ('/')
    return render(request, 'core/templates/refund.html',{'person':person ,'orders':orders}) 




def cashbalance(request ,pid):
    cash=models.Order.objects.filter( Patient_id=pid)   #order_type__in=[1, 4]
    Patientdata  =   models.Patient.objects.get(id=pid)
   
    total_price=0
    for value in cash:
        total_price += value.TotalPrice

    total_cash=0
    for value in cash:
        total_cash += value.Cash 

    total_Remmaining=0
    for value in cash:
        total_Remmaining += value.Discount
    Total_required = total_price - total_cash-total_Remmaining


    context={
           'Patientdata':Patientdata,
           'total_price':total_price,
           'cash':cash,
           'total_cash':total_cash,
           'total_Remmaining':total_Remmaining,
           'Total_required':Total_required
    }
    return render(request, 'core/templates/cashbalance.html', context)



def ballsbalance(request ,pid):
    order_all_ballses= models.Order.objects.filter( order_type__in=[1, 2,3],Patient_id=pid) 
    Patientdata  =   models.Patient.objects.get(id=pid)
  
    #Add balls efects models
    order_transfer_ballses = models.Order.objects.filter( order_type__in=[1, 2],Patient_id=pid) 

    #Cuts ballses  models
    event= Events.objects.filter(event_name=models.Patient.objects.get(pk=pid))
    order_transfer_ballses = models.Order.objects.filter( order_type=3,Patient_id=pid)

    #Add ballsese sum
    total_plus_balls_in_order=0
    for value in order_all_ballses:
        total_plus_balls_in_order += value.balls

    #Cut ballses sum    

    total_ballse_in_event=0
    for value in event:
        total_ballse_in_event +=    int(value.session_used_balls)

    order_transfer_ballses=0
    for value in range(order_transfer_ballses):
        order_transfer_ballses += value.balls

    #total cut ballses 
    total_cut_ballses =total_ballse_in_event + order_transfer_ballses

    #total balls reminning

    total_ballses_remining = total_plus_balls_in_order - total_cut_ballses

    

    objects_list = list(zip_longest(order_all_ballses, event))

    
    context={
           'Patientdata':Patientdata,
           'objects_list':objects_list,
           'total_plus_balls_in_order':total_plus_balls_in_order,
           'total_cut_ballses':total_cut_ballses,
           'total_ballses_remining':total_ballses_remining
           
           
    }
    return render(request, 'core/templates/ballsbalance.html', context)




def reserv(request):
    person  = models.Patient.objects.all()
    

    if request.method=='POST':
        Patient = models.Patient.objects.get(pk=int(request.POST.get('Patient')))
        
        
        pid  =   request.POST['Patient']


        obj = Events.objects.create(
            event_name = Patient
        )

        
        return redirect ("/")
    return render(request, 'core/templates/eventsreserv.html',{'person':person}) 
