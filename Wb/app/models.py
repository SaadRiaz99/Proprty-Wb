from django.db import models

# Create your models here.
class doctorsignup(models.Model):
    full_name = models.CharField(max_length=50)
    license_number = models.CharField(max_length=13)
    department = models.CharField(max_length=50)
    email = models.EmailField(max_length=55)
    password = models.EmailField(max_length=45)

  

class patientsignup(models.Model):
    Name = models.CharField(max_length=55)
    email = models.EmailField(max_length=55)
    password = models.EmailField(max_length=45)
    Confirm_password = models.EmailField(max_length=45)


