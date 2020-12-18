from django.shortcuts import render ,redirect

# Create your views here.
from .models import calls ,statue
from novav1.models import Patient
from .forms import callsForms
from django.utils.timezone import now
import time
import math
import datetime


def  customers_list(request):
    customers_list= Patient.objects.all()
    context={

        'customers_list':customers_list
    }


    return render(request,'calls/templates/call_list.html',context)



def make_call(request,id):
    calls_history= calls.objects.filter(Customer=id)
    if request.POST:
        form = callsForms(request.POST)
        if form.is_valid():
              newform = form.save(commit=False)
              newform.Customer_id = id
              newform.user= request.user
              if newform.save():
                return redirect('/customers_list')
              else:
               return redirect('/customers_list')
        else:
        
            return redirect('/')

        return redirect('/')
    else:
        form = callsForms()
        return render(request, 'calls/templates/new_call.html', {'form':form,'calls_history':calls_history})





def  Follow_up_calls_today(request):
    now = datetime.date.today()
    customers_list= calls.objects.filter(FollowupIN=now)
    context={

        'customers_list':customers_list
    }


    return render(request,'calls/templates/Follow_up_calls.html',context)


def  Follow_up_calls_all(request):
    now = datetime.date.today()
    customers_list= calls.objects.filter(FollowupIN__gte=now)
    context={

        'customers_list':customers_list
    }


    return render(request,'calls/templates/Follow_up_calls_all.html',context)    