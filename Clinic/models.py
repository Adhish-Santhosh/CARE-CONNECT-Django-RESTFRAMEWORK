from django.db import models

# Create your models here.

class Doctor(models.Model):

    Name = models.CharField(max_length=400)  
  
    Specialization = models.CharField(max_length=400)  
  
    Experience = models.PositiveIntegerField()  
  
    Hospital = models.CharField(max_length=400)  
  
    Qualification = models.CharField(max_length=500)  
  
    Consultation_Fee = models.PositiveIntegerField()  
  
    Available = models.BooleanField(default=True)

    def __str__(self):
        return self.Name

class AppointmentDb(models.Model):
    Patient_name = models.CharField(max_length=400)  

    phone = models.CharField(max_length=15)  

    doctor_id = models.IntegerField()  

    appointment_date=models.DateField()  

    token_number = models.PositiveIntegerField(editable=False,null=True)

    appointment_time=models.TimeField(editable=False,null=True)

    problem = models.TextField()

    status = models.CharField(max_length=200,default="Pending")

    prescription = models.TextField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.patient_name
    