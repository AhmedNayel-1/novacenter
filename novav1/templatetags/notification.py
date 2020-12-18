
from event_manage.models import Events
from django.shortcuts import render ,redirect ,get_object_or_404 

from django import template
from django.utils.safestring import mark_safe
from  datetime import date
register = template.Library()
today = date.today()

@register.simple_tag
def categories():
    items = Category.objects.filter(is_active=True).order_by('title')
    items_li = ""
    for i in items:
        items_li += """<li><a href="/category/{}">{}</a></li>""".format(i.slug, i.title)
    return mark_safe(items_li)

@register.simple_tag
def notification():
    items = Events.objects.filter(start_date__startswith=today,arrive=False)
    items_li = ""
    for i in items:
        items_li += """<li><a href="/category/{}">{}</a></li>""".format(i.event_name)
    return mark_safe(items_li)

@register.simple_tag
def navbar():
    today = date.today()
    reserv_today_count  =Events.objects.filter(start_date__startswith=today,arrive=False).count
    reserv_arrive_count =Events.objects.filter(start_date__startswith=today,arrive=True,start=False).count
    reserv_start_count  =Events.objects.filter(start_date__startswith=today,start=True).count
    
    reserv_today  =Events.objects.filter(start_date__startswith=today,arrive=False)
    reserv_arrive =Events.objects.filter(start_date__startswith=today,arrive=True,start=False)
    reserv_start  =Events.objects.filter(start_date__startswith=today,start=True)
    context={
        'reserv_today_count':reserv_today_count,
        'reserv_arrive_count':reserv_today_count,
        'reserv_start_count':reserv_today_count,
        'reserv_today':reserv_today,
        'reserv_today':reserv_today,
        'reserv_today':reserv_today,
    }


    return render (request, "core/templates/includes/navigation.html", context)