# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from novav1 import models
from novav1.models import Patient,Reservation,Packages,Device ,Order
from event_manage.models import Events
from calls.models import calls
import datetime
@login_required(login_url="/login/")
# def index(request):
#     return render(request, "index.html")

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def index(request):
    now = datetime.date.today()
    today = datetime.date.today()

    totalPatient=Patient.objects.filter(Active=True).count
    totalReservation=Reservation.objects.all().count
    totalPackages=Packages.objects.filter(Active=True).count
    totalDevice=Device.objects.filter(Active=True).count
    todatcalls=calls.objects.filter(FollowupIN=now).count


    reserv_today_count  =Events.objects.filter(start_date__startswith=today).count()
    reserv_arrive_count =Events.objects.filter(start_date__startswith=today,arrive=True,start=False).count()
    reserv_start_count  =Events.objects.filter(start_date__startswith=today,start=True).count()

    orders_p= Order.objects.filter(ordered_date__startswith=today, order_type__in=[1,2,4])
    orders_m= Order.objects.filter(ordered_date__startswith=today, order_type=5)
    total_cash_today = 0
    for cash in orders_p:
        total_cash_today += cash.Cash

    total_cash_refund =0 
    for cash in orders_m:
        total_cash_refund += cash.Cash


    net_cah=  total_cash_today - total_cash_refund







    context={
           'totalPatient':totalPatient,
           'totalReservation':totalReservation,
           'totalPackages':totalPackages,
           'totalDevice':totalDevice,
           'reserv_today_count':reserv_today_count,
           'reserv_arrive_count':reserv_arrive_count,
           'reserv_start_count':reserv_start_count,
           'total_cash_today':total_cash_today,
           'total_cash_refund':total_cash_refund,
           'net_cah':net_cah,
           'todatcalls':todatcalls,

    
    }
    return render(request,'core/templates/index.html',context)