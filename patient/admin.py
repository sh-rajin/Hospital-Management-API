from django.contrib import admin
from .models import Patient
# Register your models here.

class PatientModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_no','email', 'image')
    
    def first_name(self, obj):
        return obj.user.first_name
    
    def last_name(self, obj):
        return obj.user.last_name
    
    def email(self, obj):
        return obj.user.email
    
admin.site.register(Patient, PatientModelAdmin)
