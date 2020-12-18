from django.db import models

# Create your models here.
from datetime import datetime ,timedelta
from django.utils.timezone import now
from novav1.models import Patient
from django.contrib.auth.models import User
import time
import math
import datetime
from django.conf import settings
LABEL_CHOICES = (
    
    (1, '1 day'),
    (2, '2days'),
    (3, '3days'),
    (4, '4days'),
    (5, '5days'),
    (6, '6days'),
    (7, 'week'),
    (14, 'weeks'),
    (30, 'Month')
)

class statue(models.Model):
    statue=models.CharField(max_length=10)


    def __str__(self):
        return str(self.statue)


class calls(models.Model):
    Customer     = models.ForeignKey("novav1.Patient", on_delete=models.CASCADE)
    user         = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True,null=True)
    Note         = models.TextField(max_length=100)
    Statue       = models.ForeignKey("statue", on_delete=models.CASCADE)
    Calldate     = models.DateField(default=datetime.datetime.now,blank=True,null=True)
    Followup     = models.IntegerField(choices=LABEL_CHOICES,blank=True,null=True)
    FollowupIN = models.DateField(blank=True,null=True)

    def __str__(self):
        return str(self.Customer)


    def FollowupDate(self):
        sd = self.Calldate
        days = self.Followup
        ed = datetime.timedelta(days=-days)
        print(ed)
        Followupdate = sd-ed
                
        return Followupdate       
                
            
            

    def save(self, *args, **kwargs):
        if self.Followup > 0 :
            self.FollowupIN = self.FollowupDate()
        
        super(calls, self).save(*args, **kwargs)    