from django.shortcuts import render

# Create your views here.
from .models import names,Events



def TestNames(request):
    data= names.objects.all()
    context={
             'data':data
    }
    return render(request,'reservation.html',context)


   
import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import EntryCreationForm
from .models import Entry, Language
from datetime import *

def home(request):
    form = EntryCreationForm(instance=Entry.objects.first())
    if request.is_ajax():
        term = request.GET.get('term')
        languages = Language.objects.all().filter(title__icontains=term)
        return JsonResponse(list(languages.values()), list(names.values()),safe=False)
    if request.method == 'POST':
        form = EntryCreationForm(request.POST, instance=Entry.objects.first())
        if form.is_valid():
            form.save()
            return redirect('select2')
    return render(request, 'test2.html', {'form': form})

# def calendar(request):
#     all_events = Events.objects.all()
#     context = {
#         "events":all_events,
#     }
#     return render(request,'calendardata.html',context)
        



def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'fullcalander.html',context)

def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)