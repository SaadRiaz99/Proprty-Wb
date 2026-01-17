from django.contrib import admin
from django.urls import path , include
from app import views

urlpatterns = [
    path('', views.index, name = 'index'),
    
    path('index.html', views.index, name = 'index'),
    path('Patientsignup.html', views.patientsignup, name = 'Patientsignup'),
    path('doctorsignup.html', views.doctorsignup , name = 'doctorsignup'),
    path('patientlogin.html', views.patientlogin , name = 'patientlogin'),
    path('dashboard.html', views.dashboard , name = 'dashboard'),
    path('base.html', views.base , name = 'base'),
    
]
