from django.shortcuts import render, redirect
from pages.forms import *
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return redirect('login')

    return render(request, 'login.html')

# def register(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')

#     else:

#         form = SignUpForm()
        
#     context = {
#             'form': form
#         }
#     return render(request, 'register.html', context)


def patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:

        form = PatientForm()
        
    context = {
            'form': form
        }
    return render(request, 'register.html', context)

def doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:

        form = DoctorForm()
        
    context = {
            'form': form
        }
    return render(request, 'register.html', context)

def dashboard(request):
    return render(request, 'dashboard.html')