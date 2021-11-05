from django.db import models
from django.contrib.auth.models import User
        
# Create your models here.
class Patient(models.Model):

    BLOOD_GROUP = [
        ('A', 'A'),
        ('A+', 'A+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('AB', 'AB'),
        ('0-', '0-'),
        ('0+', '0+'),
    ]
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150, null=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=100)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUP)
   
    def __str__(self):
        return self.user.username


class Specialization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username

class Doctor(models.Model):
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'), ]
 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=100)
    dob = models.DateField()
    image = models.FileField(null=True)
    experience = models.CharField(max_length=250, null=True)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=GENDER)

    def __str__(self):
        return self.user.username



       



class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    appointment_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.doctor.user.username+ " "+self.patient.user.username



