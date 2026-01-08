from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
     return render(request,   'index.html')

def patientsignup(request):
     return render(request, 'patientsignup.html')     

def doctorsignup(request):
     return render(request , 'doctorsignup.html')

def patientlogin(request):
     return render(request , 'doctorsignup.html')