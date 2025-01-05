from django.db import models
from patient.models import Patient
from doctor.models import Doctor, AvailableTime
# Create your models here.

APPOINMENT_TYPES = (
    ('Online', 'Online'),
    ('Offline', 'Offline'),
)
APPOINMENT_STATUS = (
    ('Running', 'Running'),
    ('Pending', 'Pending'),
    ('Completed', 'Completed'),
)

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=10, choices=APPOINMENT_TYPES)
    appointment_status = models.CharField(max_length=10, choices=APPOINMENT_STATUS, default= "Pending")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete=models.CASCADE)
    cancel = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.patient.user.first_name} - {self.doctor.user.first_name} - {self.time}"


