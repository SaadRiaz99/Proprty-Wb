from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import doctorsignup as DoctorModel
from .models import patientsignup as PatientModel
from django.contrib.auth.decorators import login_required

# ----------------- Doctor Signup -----------------
def doctorsignup(request):
    if request.method == "POST":
        full_name = request.POST.get('full_name')
        license_number = request.POST.get('license_number')
        department = request.POST.get('department')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'doctorsignup.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered")
            return render(request, 'doctorsignup.html')

        user = User.objects.create_user(username=email, email=email, password=password)
        DoctorModel.objects.create(
            user=user,
            full_name=full_name,
            license_number=license_number,
            department=department,
            email=email
        )

        messages.success(request, "Signup successful! Please login.")
        return redirect('index')

    return render(request, 'doctorsignup.html')


# ----------------- Doctor Login -----------------
def index(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            # Ensure user is a doctor
            if DoctorModel.objects.filter(user=user).exists():
                login(request, user)
                messages.success(request, "Doctor login successful!")
                return redirect('dashboard')
            else:
                messages.error(request, "This is not a doctor account")
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'index.html')



def patientsignup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return render(request, 'Patientsignup.html')

        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered")
            return render(request, 'Patientsignup.html')

        user = User.objects.create_user(username=email, email=email, password=password)
        PatientModel.objects.create(user=user, Name=name, email=email)

        messages.success(request, "Signup successful! Please login.")
        return redirect('patientlogin')

    return render(request, 'Patientsignup.html')


# ----------------- Patient Login -----------------
def patientlogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:
            if PatientModel.objects.filter(user=user).exists():
                login(request, user)
                messages.success(request, "Patient login successful!")
                return redirect('dashboard')
            else:
                messages.error(request, "This is not a patient account")
        else:
            messages.error(request, "Invalid email or password")

    return render(request, 'patientlogin.html')



@login_required
def dashboard(request):
    return render(request, 'dashboard.html')



def base(request):
    return render(request, 'base.html')

def patientdashboard(request):
    return render(request, 'Web1.html')