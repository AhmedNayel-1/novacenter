# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from novav1.models import  Branch
# Create your models here.

class Section(models.Model):
    section_name=models.CharField(max_length=50)

    def __str__ (self):
        return self.section_name

class User(AbstractUser):
    section_name = models.ForeignKey("Section", on_delete=models.CASCADE,blank=True, null=True)
    branch       = models.ForeignKey("novav1.Branch",  on_delete=models.CASCADE,blank=True, null=True)