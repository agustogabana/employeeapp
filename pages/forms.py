from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from pages.models import *
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'

class AppointForm(forms.ModelForm):
    class Meta:
        model = Appointment 
        fields = '__all__'