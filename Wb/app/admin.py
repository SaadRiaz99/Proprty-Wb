from django.contrib import admin
from .models import doctorsignup, patientsignup

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'license_number', 'department', 'user')
    search_fields = ('full_name', 'email', 'license_number', 'department')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('Name', 'email', 'user')
    search_fields = ('Name', 'email')

admin.site.register(doctorsignup, DoctorAdmin)
admin.site.register(patientsignup, PatientAdmin)
