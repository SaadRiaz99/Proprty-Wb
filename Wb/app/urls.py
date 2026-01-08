from django.contrib import admin
from django.urls import path , include
from app import views

urlpatterns = [
    path('index.html', views.index, name = 'index'),
    path('patientsignup.html', views.patientsignup, name = 'patientsignup'),
    path('doctorsignup.html', views.doctorsignup , name = 'doctorsignup'),
    path('patientlogin.html', views.patientlogin , name = 'patientlogin'),
    
]