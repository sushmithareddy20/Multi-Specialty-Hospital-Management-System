from django.contrib import admin
from .models import Doctor,Patient,Appointment,PatientDischargeDetails
from django.contrib.auth import logout
from django.shortcuts import redirect

def admin_logout_view(request):
    logout(request)
    # Redirect to the home page after logout
    return redirect('home')  # Assuming 'home' is the name of your home page URL pattern

# Register your models here.
class DoctorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Doctor, DoctorAdmin)

class PatientAdmin(admin.ModelAdmin):
    pass
admin.site.register(Patient, PatientAdmin)

class AppointmentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Appointment, AppointmentAdmin)

class PatientDischargeDetailsAdmin(admin.ModelAdmin):
    pass
admin.site.register(PatientDischargeDetails, PatientDischargeDetailsAdmin)