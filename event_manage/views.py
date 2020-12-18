from django.shortcuts import render ,redirect ,get_object_or_404 
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic
from .models import Events , CrudUser ,EventType ,deviceparameters ,Event
from novav1.models import Patient ,DoctorIn , pricing ,Patient ,Branch,DoctorIn,pricing,Clinc,Category
from .forms  import EventForm ,ArriveForm , SessionDetail ,callsFormsEvents,ParametersForms
from django.views.generic import TemplateView, View, DeleteView
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from datetime import datetime ,date ,timedelta
from .filter import EventsFilter
from django.db.models import Q 
from django.db.models import Max ,F
from itertools import zip_longest 
from .utils import send_whatsapp_messages , send_sms_messages ,send_sms_messages_auto



#Create your views here.

# def event(request):
#     all_events = Events.objects.all()
#     get_event_types = Events.objects.only('event_type')

#     # if filters applied then get parameter and filter based on condition else return object
#     # if request.GET:  
#     #     event_arr = []
#     #     if request.GET.get('event_type') == "all":#
#     #         all_events = Events.objects.all()
#     #     else:   
#     #         all_events = Events.objects.filter(event_type__icontains=request.GET.get('event_type'))
            
#     #     for i in all_events:
#     #         event_sub_arr = {}
#     #         event_sub_arr['title'] = i.event_name
#     #         start_date = datetime.datetime.strptime(str(i.start_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#     #         end_date = datetime.datetime.strptime(str(i.end_date.date()), "%Y-%m-%d").strftime("%Y-%m-%d")
#     #         event_sub_arr['start'] = start_date
#     #         event_sub_arr['end'] = end_date
#     #         event_arr.append(event_sub_arr)
#     #     return HttpResponse(json.dumps(event_arr))

#     context = {
#         "events":all_events,
#         #"get_event_types":get_event_types,

#     }
#     return render(request,'core/templates/calendar.html',context)


def event(request):
    all_events = Events.objects.all()
    get_event_types = Events.objects.only('event_type')
    pe  = Patient.objects.all()
    ev   = Events.objects.all()
    Cl   = Clinc.objects.all()
    Doc   = DoctorIn.objects.all()
    Br  = Branch.objects.all()
    pr   = pricing.objects.all()
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    filter = EventsFilter(request.GET, queryset=Events.objects.all())
    
    context = {
        "events":all_events,
        'pe':pe,
        'Cl':Cl,
        'Doc':Doc,
        'Br':Br,
        'pr':pr,
        'filter':filter,


    }
    return render(request,'core/templates/calendar.html',context)



def calendar(request):
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'core/templates/calendar2.html',context)

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





class CreateCrudUser(View):
    def  get(self, request):
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)    




def add_event_to_end(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    Events = Events(name=str(event_name), start=start_date, end=end_date)
    Events.save()
    data = {}
    return JsonResponse(data)        


# class newevent(View):
#     def  get(self, request):
def newevent(request):
    if request.method=='POST':
        event_name     = Patient.objects.get(pk=request.POST.get('Patient'))
        start_date     = request.POST['start']
        end_date       = request.POST['end']
        session_clinic = Clinc.objects.get(pk=request.POST.get('clinic'))
        event_doctor   = DoctorIn.objects.get(pk=request.POST.get('doctor'))
        branch_event   = Branch.objects.get(pk=request.POST.get('branch'))
        event_area     = request.POST['area']    #pricing.objects.get(pk=request.POST.get('area'))
        user           = request.user
        

        # obj = Events.objects.create(
        #     event_name = event_name,
        #     start_date = start_date,
        #     end_date = end_date,
        #     session_clinic=session_clinic,
        #     event_doctor=event_doctor,
        #     branch_event=branch_event,
        #     #event_area=event_area
        # )
        obj = Events(
        event_name = event_name,
        start_date = start_date,
        end_date = end_date,
        session_clinic=session_clinic,
        event_doctor=event_doctor,
        branch_event=branch_event,
        #event_area=event_area

        )

        obj.save()
        

        obj.event_area.add(event_area)
        

        # areas = pricing.objects.get(pk=int(request.POST['area']))
        # for areas in areas:
        #     obj.event_area.add(areas)

        return redirect ('/event')
    return redirect ('/event')




       




# class EventCreateView(generic.CreateView):
#     template_name="event_manage/templates/event_form.html"
#     model = Events
#     form_class = EventForm
#     success_url = "/"


class ArriveCreateView(generic.CreateView):
    template_name="event_manage/templates/arrive_form.html"
    model = Events
    form_class = ArriveForm
    success_url = "/"    
    




def EventCreateView(request):
    person  = Patient.objects.all()
    event   = Events.objects.all()

    if request.method=='POST':
        Patients  = Patient.objects.get(pk=int(request.POST['Patient']))
        to= Patients.PatientMobile1
        pname= Patients.PatientName
        
        event_name  = Patient.objects.get(id=int(request.POST.get('Patient')))
        start_date  = request.POST['start_date']
        end_date    = request.POST['end_date']
        # #user = request.user
        
        obj = Events.objects.create(
            event_name = event_name,
            start_date = start_date,
            end_date = end_date,
            

        )

        # body = "لقد تم الحجز يوم Nova center " + str(start_date) + str(pname) + " باسم"+ " "
        body = f' نوفاسنتر{start_date}بتاريح {pname} تم الحجز باسم '
        #send_whatsapp_messages(body,to)
        send_sms_messages(to)
        send_sms_messages_auto(body,to)

        print(start_date)
        return redirect ('/event')
    return render(request, 'event_manage/templates/event_form_git_test.html',{'person':person})



def reception_all_reserv(request):
    today = date.today()
    reserv_today  =Events.objects.filter(start_date__startswith=today,arrive=False)
    
    print(reserv_today)
    context={
        'reserv_today':reserv_today,
           
    }

    return render(request,'event_manage/templates/reseptions.html',context)

            
    

def reception_reserv_arrive(request):
    today = date.today()
   
    reserv_arrive =Events.objects.filter(start_date__startswith=today,arrive=True,start=False)
    
    
    context={
        
        'reserv_arrive':reserv_arrive,
            
    }

    return render(request,'event_manage/templates/reseptions_arrive.html',context)

def reception_reserv_srart(request):
    today = date.today()
   
    
    reserv_start  =Events.objects.filter(arrivetime__startswith=today,start=True)
    print(reserv_start)
    context={
        
        'reserv_start':reserv_start,
            
    }

    return render(request,'event_manage/templates/reseptions_start.html',context)



def onofarrive(requset,id):
    a = get_object_or_404(Events, event_id=id)
    a.arrive = True
    a.arrivetime = datetime.now()
    a.save()
    return redirect("event_manage:reception_reserv_arrive")     

# def onofstart(requset,id):
#     a = get_object_or_404(Events, event_id=id)
#     a.start = True
#     a.save()
#     return redirect("event_manage:reception_reserv_srart")   






def sessionDetail(request,id):
    events = Events.objects.get(event_id=id)
    event_name=events.event_name
    eventsparts= events.event_area
    targetid= id -1
    eventsprametars=deviceparameters.objects.filter(Patient_name=event_name)
    #eventsprametars=deviceparameters.objects.filter(Patient_name=event_name,event_id=targetid).order_by('-event_id')                    
    #eventsprametars=deviceparameters.objects.order_by('Patient_name__PatientName', '-Date').distinct('Patient_name__PatientName')
    #eventsprametars=deviceparameters.objects.annotate(max_date=Max('part_id__deviceparameters__Date')).filter(Date=F('max_date'),Patient_name=event_name,part_id=eventsparts)
    if request.method == 'POST':
        form = SessionDetail(request.POST, instance=events)
        if form.is_valid():
           newform = form.save(commit=False)
           newform.start = True
           newform.start_session = datetime.now()
           newform.save()
           return redirect("event_manage:reception_reserv_srart")
           
    else:
        form = SessionDetail(instance=events)
    return render(request, 'event_manage/templates/session.html',{'form':form,'events':events,'eventsprametars':eventsprametars})




def balls_entry(request,event_id):
    if request.method=='POST':
      a = get_object_or_404(Events, event_id=event_id)
      a.session_used_balls = request.POST['used_balls']
      a.session_end =datetime.now()
      a.end =True
      a.save()


      

    #   data= Events(event_id=event_id,session_used_balls=session_used_balls)
    #   data.save

      return redirect("event_manage:reception_all_reserv")



def filter(request): 
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    filter = EventsFilter(request.GET, queryset=Events.objects.filter(start_date__startswith=tomorrow))
    events= Events.objects.all()
   
    print(today)
    context={
               'events':events,
               'filter': filter,
               'tomorrow':tomorrow
    }
    return render(request, 'table.html', context)      



def eventfilter(request):
    #Patients= models.Patient.objects.all
    DoctorIns   = DoctorIn.objects.all()
    events_type   = EventType.objects.all()
    today = datetime.now().date()
    tomorrow = today + timedelta(1)

    if request.method == 'GET':
            start_date   = tomorrow #request.GET.get('start', None)
            end_date     = request.GET.get('end', None)
            event_type   = request.GET.get('doctor', None)
            event_doctor = request.GET.get('events', None)
            submitbutton= request.GET.get('submit', None)

            #if request is not None:
            lookups= Q(start_date__icontains=start_date) | Q(end_date__icontains=end_date)|  Q(event_doctor__icontains=event_type)|Q(event_doctor__icontains=event_doctor)
                            
                            
                            

            results= Events.objects.filter(lookups).distinct()

            context={'results': results,
                    'submitbutton': submitbutton,
                    'Patients':Patients
                    }

            return render(request, 'core/templates/search.html', context)

            # else:
            #      return render(request, 'core/templates/search.html',{'Patients':Patients,'events_type':events_type,'DoctorIns':DoctorIns})

    else:
        return render(request, 'core/templates/search.html',{'Patients':Patients,'events_type':events_type,'DoctorIns':DoctorIns}) 


def make_call_for_events(request,id):
    event_get_data = Events.objects.get(event_id=id)
    eventdata      =Events.objects.filter(event_id=id)
    if request.POST:
        form = callsFormsEvents(request.POST, instance=event_get_data)
        if form.is_valid():
              newform = form.save(commit=False)
              newform.event_id = id
              newform.user= request.user
              if newform.save():
                return redirect('event_manage:eventfilter')
              else:
               return redirect('event_manage:eventfilter')
        else:
        
            return redirect('event_manage:eventfilter')

        return redirect('event_manage:eventfilter')
    else:
        form = callsFormsEvents()
        print(eventdata)
        return render(request, 'event_manage/templates/event_call.html', {'form':form,'eventdata':eventdata})



def dvice_prametars(request,id):
    eventsprametars=deviceparameters.objects.filter(Patient_name=id)
    #eventsprametars=parameters.objects.filter(event_id=id)#.order_by('-id')[0] 

    context={

        'eventsprametars':eventsprametars
    }   
    print(eventsprametars)
    return render(request, 'event_manage/templates/receipt.html', context)




def paramentry(request,id):
    # events = Events.objects.get(event_id=id)
    # event_name=events.event_name

    # eventsprametars=deviceparameters.objects.annotate(max_date=Max('part_id__deviceparameters__Date')).filter(Date=F('max_date'),Patient_name=event_name)
    if request.method=='POST':
        Patient_name     = Patient.objects.get(pk=request.POST.get('Patient'))
        part        = pricing.objects.get(pk=request.POST.get('area'))
        
        CandelaAlex = request.POST['CandelaAlex']
        DekaAlex    = request.POST['DekaAlex']
        DekaMoveo   = request.POST['DekaMoveo']
        Joule       = request.POST['Joule']
        msec        = request.POST['msec']
        PulseCount  = request.POST['PulseCount']
        OperatorName=DoctorIn.objects.get(pk=request.POST.get('doctor'))
        user           = request.user
        

        obj = deviceparameters.objects.create(
            Patient_name = Patient_name,
            part = part,
            CandelaAlex = CandelaAlex,
            DekaAlex=DekaAlex,
            Joule=Joule,
            msec=msec,
            PulseCount=PulseCount,
            OperatorName=OperatorName,
            user=user,

        )
        
        print(request)
        return redirect ('/')
    return render(request, 'event_manage/templates/prametars_entry.html', {'eventsprametars':eventsprametars,})



def prametersreport(request,id):
    events = Events.objects.get(event_id=id)
    event_name=events.event_name
    eventsarea=Events.objects.filter(event_id=id)
    eventsprametars=deviceparameters.objects.annotate(max_date=Max('part_id__deviceparameters__Date')).filter(Date=F('max_date'),Patient_name=event_name)
    if request.method=='POST':
        Patient_name     = Patient.objects.get(pk=request.POST.get('Patient'))
        part        = pricing.objects.get(pk=request.POST.get('area'))
        
        CandelaAlex = request.POST['CandelaAlex']
        DekaAlex    = request.POST['DekaAlex']
        DekaMoveo   = request.POST['DekaMoveo']
        Joule       = request.POST['Joule']
        msec        = request.POST['msec']
        PulseCount  = request.POST['PulseCount']
        OperatorName=DoctorIn.objects.get(pk=request.POST.get('doctor'))
        user           = request.user
        

        obj = deviceparameters.objects.create(
            Patient_name = Patient_name,
            part = part,
            CandelaAlex = CandelaAlex,
            DekaAlex=DekaAlex,
            Joule=Joule,
            msec=msec,
            PulseCount=PulseCount,
            OperatorName=OperatorName,
            user=user,


        )
    context={
        'events':events,
        'eventsprametars':eventsprametars,
        'eventsarea':eventsarea

    }


    return render(request, 'event_manage/templates/prametars_entry.html', context)



def EventCreateView_new(request):
    pe  = Patient.objects.all()
    ev   = Events.objects.all()
    Cl   = Clinc.objects.all()
    Doc   = DoctorIn.objects.all()
    Br  = Branch.objects.all()
    pr   = pricing.objects.all()
    cat   = Category.objects.all()

    if request.method=='POST':
        event_name     = Patient.objects.get(pk=request.POST.get('Patient'))
        start_date     = request.POST['start_date']
        end_date       = request.POST['end_date']
        session_clinic = Clinc.objects.get(pk=request.POST.get('clinic'))
        event_doctor   = DoctorIn.objects.get(pk=request.POST.get('doctor'))
        branch_event   = Branch.objects.get(pk=request.POST.get('branch'))
        event_area     = pricing.objects.get(pk=request.POST.get('area'))
        category       = Category.objects.get(pk=request.POST.get('cat'))
        user           = request.user
        

        obj = Events.objects.create(
            event_name = event_name,
            start_date = start_date,
            end_date = end_date,
            session_clinic=session_clinic,
            event_doctor=event_doctor,
            branch_event=branch_event,
            event_service=category
            #event_area=event_area

        )
        obj.event_area.add(event_area)
        # obj = Events(
        #     event_name = event_name,
        #     start_date = start_date,
        #     end_date = end_date,
        #     session_clinic=session_clinic,
        #     event_doctor=event_doctor,
        #     branch_event=branch_event,
        #     #event_area=event_area

        # )
        # obj.save()
        #obj.event_area.add()
        # areas = pricing.objects.get(id=event_area)
        # for user in areas:
        #     obj.event_area.add(areas)

        # context = {
        #         'person':person,
        #         'Clincs':Clincs,
        #         'DoctorIns':DoctorIns,
        #         'Branchs':Branchs,
        #         'pricings':pricings,

        # }

        print(request)
        return redirect ('/event')
    return render(request, 'event_manage/templates/event_form_new.html', {
                'pe':pe,
                'Cl':Cl,
                'Doc':Doc,
                'Br':Br,
                'pr':pr,
                'cat':cat

        })

def calendertest(request):
    context={}
    return render(request, 'event_manage/templates/caltest.html',context )        





def allInOneView(request,part_id,id):

    part_id = part_id
    Pat_deviceparameters=deviceparameters.objects.filter(part_id=part_id,Patient_name_id=id)
    parts=pricing.objects.all()
    objects_list = list(zip_longest(Pat_deviceparameters, parts))
    Patients= Patient.objects.get(pk=id)
    
    try:
        parametername= get_object_or_404 (pricing ,pk=part_id)
    except ObjectDoesNotExist:
        messages.info(request, "Item was added to your cart.")
    
    par =  pricing.objects.raw('select * from novav1_pricing '
                                          'left join (select * from event_manage_deviceparameters where  Patient_name_id=%s) '
                                          ,[id])
    try:
        session = deviceparameters.objects.get(part_id=part_id,Patient_name_id=id)
    except ObjectDoesNotExist:
        session = None

    
    """
    A subclass of ModelForm can accept an existing model instance 
    as the keyword argument instance; 
    if this is supplied, save() will update that instance. 
    If it's not supplied, save() will create a new instance of the specified model.
    """
    
    form = ParametersForms(instance=session)
    if part_id != 0 :
        if request.method == 'POST':
            form = ParametersForms(request.POST, instance=session)
            if form.is_valid():
                newform = form.save(commit=False)
                newform.Patient_name = Patient.objects.get(pk=id)
                newform.Date = datetime.now()     
                newform.part = pricing.objects.get(pk=part_id)
                newform.save()
                
            return HttpResponseRedirect(request.path)
    else:
        messages.info(request, "Item was added to your cart.")

    return render(request  ,'event_manage/templates/editor.html', {'form': form,'Pat_deviceparameters':Pat_deviceparameters,'parts':parts,'objects_list':objects_list,'par':par,'Patients':Patients,'parametername':parametername})