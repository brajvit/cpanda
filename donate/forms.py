from __future__ import unicode_literals
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from datetimewidget.widgets import DateTimeWidget, DateWidget, TimeWidget 
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model
from . import models
from .models import Product, Service, Event

User = get_user_model()

class PostForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title', 'description', 'active', 'quantity','address', 'zip_Code', 'expire_date', )


class Service1Form(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('title', 'description', 'active', 'duraction', 'address', 'zip_Code', 'expire_date', )


class DocumentForm(forms.Form):
    
    title = forms.CharField(
        label='Title', widget=forms.TextInput(attrs={'placeholder': 'Enter title'})
    )
    
    description = forms.CharField(
        label='Description', widget=forms.TextInput(attrs={'placeholder': 'Tell more about your donating item'})
    )   
   
    quantity = forms.IntegerField(
        label='Quantity', widget=forms.TextInput(attrs={'placeholder': 'No. of items you donating'})
    )
    zip_Code = forms.CharField(
        label='Zipcode', widget=forms.TextInput(attrs={'placeholder': 'Zipcode of your area'})
    )
    docfile = forms.FileField(
        label='Product Image '
    )
    address = forms.CharField(
        label='Place Where Available', widget=forms.TextInput(attrs={'placeholder': 'Your loaction where item available '})
    )
    expire_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    active = forms.BooleanField(
        label='Are you sure to publish'
    )

class ServiceForm(forms.Form): 
	
    title = forms.CharField(
        label='Title', widget=forms.TextInput(attrs={'placeholder': 'Provide service name'})
    )
    
    description = forms.CharField(
        label='Description', widget=forms.TextInput(attrs={'placeholder': 'Some details about your service'})
    )  
    
    duraction = forms.CharField(
        label='Duration', widget=forms.TextInput(attrs={'placeholder': 'Time  schedule of service'})
    )
    zip_Code = forms.CharField(
        label='Zipcode',widget=forms.TextInput(attrs={'placeholder': 'Your area zipcode'})
    )
    docfile = forms.FileField(
        label='Select Service Image'
    )
    address = forms.CharField(
        label='Place', widget=forms.TextInput(attrs={'placeholder': 'place where service offer'})
    )
    expire_date = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))

    active = forms.BooleanField(
        label='Are you sure to publish'
    )
   
class EventForm(forms.Form):
    eventtype = forms.CharField(required=False,label='Title', widget=forms.TextInput(attrs={'placeholder': 'Title of event'}))
    snap = forms.FileField(required=False,label='Event Look-up Picture ')    
    date_event = forms.DateTimeField(label='Event Date',widget=DateTimeWidget(usel10n=True, bootstrap_version=3))    
    description = forms.CharField(label='Description', widget=forms.TextInput(attrs={'placeholder': 'Give some overview of your event'}))
    place = forms.CharField(
        label='Place', widget=forms.TextInput(attrs={'placeholder': 'Location of your event offer '})
    )    
    duration = forms.TimeField(widget=TimeWidget(usel10n=True, bootstrap_version=3))
    dresscode = forms.BooleanField(
        label='Event Dress Code Allow'
    )  

class EvtForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('eventtype', 'snap', 'date_event', 'description','place', 'dresscode', 'duration', )
  
    
    
