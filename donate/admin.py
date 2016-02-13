from django.contrib import admin
from .models import Product, Service, Event

# Register your models here.

admin.site.register(Event)
admin.site.register(Product)
admin.site.register(Service)

