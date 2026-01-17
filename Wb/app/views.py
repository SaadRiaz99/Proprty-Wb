from django.shortcuts import render, HttpResponse, redirect
from .models import doctorsignup as doctorsignupData 
from .models import patientsignup as  patientsignupData
from django.contrib import messages


# Create your views here.

def index(request):    
     return render(request,   'index.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

def patientsignup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        
        if password != confirm_password:
            messages.error(request, "Password and Confirm Password do not match")
            return render(request, 'Patientsignup.html')

       
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered")
            return render(request, 'Patientsignup.html')

        user = User.objects.create(
            username=email,
            email=email,
            password=make_password(password)
        )

        messages.success(request, "Signup successful! Please login.")
        return redirect('patientlogin.html')

    return render(request, 'Patientsignup.html')
  

def doctorsignup(request):
     if request.method == "POST":
          Doctor = request.POST.get('full_name')
          license_Num = request.POST.get('license_number')
          Email = request.POST.get('email')
          Department = request.POST.get('department')          
          Password = request.POST.get('password')
          
          signup = doctorsignupData(
               full_name = Doctor,
               license_number = license_Num,
               department = Department,
               email  = Email,
               password = Password
          )
          signup.save()
     return render(request , 'doctorsignup.html')

def patientlogin(request):
     return render(request , 'patientlogin.html')

def base(request):
     return render(request , 'base.html')

def dashboard(request):
     return render(request , 'dashboard.html')     