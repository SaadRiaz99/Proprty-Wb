from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Doctor
    path('index.html', views.index, name='index'),
    path('doctorsignup.html', views.doctorsignup, name='doctorsignup'),

    # Patient
    path('Patientsignup.html', views.patientsignup, name='patientsignup'),
    path('patientlogin.html', views.patientlogin, name='patientlogin'),

    # Pages
    path('dashboard.html', views.dashboard, name='dashboard'),
    path('base.html', views.base, name='base'),
    path('Web1.html', views.patientdashboard, name='patientdashboard'),
]
