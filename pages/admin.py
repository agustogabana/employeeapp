from django.contrib import admin
from pages.models import *
# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Appointment)
