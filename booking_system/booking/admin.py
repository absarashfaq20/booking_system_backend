from django.contrib import admin
from .models import Service, ServiceProvider, TimeSlot, Appointment

admin.site.register(Service)
admin.site.register(ServiceProvider)
admin.site.register(TimeSlot)
admin.site.register(Appointment)