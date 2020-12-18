from django.db import models
from novav1.models import  DoctorIn , pricing ,Patient ,Branch,DoctorIn,pricing,Clinc

# Create your models here.
class EventType(models.Model):
    status=models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.status)


class   deviceparameters(models.Model):
    #event        = models.ForeignKey("Events", on_delete=models.CASCADE,null=True,blank=True)
    Patient_name = models.ForeignKey("novav1.Patient",on_delete=models.CASCADE,null=True,blank=True,db_constraint=False)
    part         = models.ForeignKey("novav1.pricing",on_delete=models.CASCADE,null=True,blank=True,db_constraint=False)
    Date         = models.DateField( auto_now=False)
    CandelaAlex  = models.BooleanField()
    DekaAlex     = models.BooleanField()
    DekaMoveo    = models.BooleanField()
    Joule        = models.IntegerField()
    msec         = models.IntegerField()
    PulseCount   = models.IntegerField()
    OperatorName = models.ForeignKey("novav1.DoctorIn",related_name="Operator_Name" , on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.Patient_name)



class Events(models.Model):
    event_id        = models.AutoField(primary_key=True)
    #event_name     = models.CharField(max_length=255,null=True,blank=True)
    event_name      = models.ForeignKey("novav1.Patient",  on_delete=models.CASCADE,null=True,blank=True,db_constraint=False)
    start_date      = models.DateTimeField(null=True,blank=True)
    end_date        = models.DateTimeField(null=True,blank=True)
    event_type      = models.ForeignKey("EventType", on_delete=models.CASCADE,null=True,blank=True,default=0,db_constraint=False)
    allDay          = models.BooleanField(default=False)
    url             = models.URLField( max_length=200,null=True,blank=True)
    backgroundColor = models.CharField(max_length=50,null=True,blank=True)
    borderColor     = models.CharField(max_length=50,null=True,blank=True)
    event_doctor    = models.ForeignKey("novav1.DoctorIn", related_name="event_doctor",  on_delete=models.CASCADE,null=True,blank=True,db_constraint=False) 
    event_clinic  = models.ForeignKey("novav1.Clinc", related_name="event_clinic",  on_delete=models.CASCADE,blank=True, null=True,db_constraint=False)
    branch_event    = models.ForeignKey("novav1.Branch", related_name="branch_event", on_delete=models.CASCADE,null=True,blank=True,db_constraint=False)
    event_note      = models.TextField(null=True,blank=True)
    event_area      = models.ManyToManyField("novav1.pricing",blank=True, null=True,db_constraint=False)
    event_service   = models.ForeignKey("novav1.Category", related_name="event_Category",  on_delete=models.CASCADE,null=True,blank=True,db_constraint=False) 
    arrive          = models.BooleanField(default=False)
    arrivetime      = models.DateTimeField(null=True,blank=True)  
    arrivetime2     = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    start           = models.BooleanField(default=False)
    start_session   = models.DateTimeField(null=True,blank=True)
    end             = models.BooleanField(default=False)
    session_end     = models.DateTimeField(null=True,blank=True)
    session_clinic  = models.ForeignKey("novav1.Clinc", related_name="session_clinic",  on_delete=models.CASCADE,blank=True, null=True,db_constraint=False)
    session_doctor  = models.ForeignKey("novav1.DoctorIn", related_name="session_doctor",  on_delete=models.CASCADE,blank=True, null=True,db_constraint=False)
    session_area    = models.ManyToManyField("novav1.pricing",related_name="session_area",  blank=True, null=True,db_constraint=False)
    session_used_balls= models.IntegerField(blank=True, null=True)
    session_branch= models.ForeignKey("novav1.Branch", related_name="session_branch", on_delete=models.CASCADE,blank=True, null=True,db_constraint=False)
    #session_parameters   = models.ForeignKey("parameters", related_name="session_parameters", on_delete=models.CASCADE,blank=True, null=True)





    def __str__(self):
        return str(self.event_name)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return str(self.name)      

  




class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)




