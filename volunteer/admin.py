from django.contrib import admin

from .models import VolunteerJob, VolunteerApplication

admin.site.register(VolunteerJob)
admin.site.register(VolunteerApplication)
