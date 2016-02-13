from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
# Create your models here.


class Product(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    title  = models.CharField(max_length=120)
    docfile = models.FileField(upload_to='Product/%Y/%m/%d')
    #description = models.CharField(max_length=120)
    description = models.CharField(default=False, max_length=160)
    active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    zip_Code = models.CharField(blank = True, max_length=6)
    address = models.CharField(default=False, max_length=60)
    date_created = models.DateTimeField(default=timezone.now)
    date_Update = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField(blank=True, null=True)
      
    class Meta:
        verbose_name = ("Product")
        verbose_name_plural = ("products")
        ordering = ("docfile",)

    def __unicode__(self):
        return self.docfile.path

class Service(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    title  = models.CharField(max_length=120)
    docfile = models.FileField(upload_to='Service/%Y/%m/%d')
    description = models.CharField(default=False, max_length=160)
    active = models.BooleanField(default=True)
    duraction  = models.CharField(max_length=120)
    zip_Code = models.CharField(max_length=6)
    address = models.CharField(default=False, max_length=60)
    date_created = models.DateTimeField(default=timezone.now)
    date_Update = models.DateTimeField(default=timezone.now)
    expire_date = models.DateTimeField()
    
    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("services")
    def __unicode__(self):
        return (self.title)

class Event(models.Model):
    user =  models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True)
    snap = models.FileField(upload_to='Event/%Y/%m/%d',blank=True, null=True)
    eventtype = models.CharField(max_length=200,null=False)
    date_created = models.DateTimeField(default=timezone.now)
    date_event = models.DateTimeField(default=False)
    dresscode = models.BooleanField(default=False)
    duration = models.TimeField(blank=True, null=True)
    description= models.CharField(max_length=400)
    place = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("events")
    def __unicode__(self):
        return (self.eventtype)





