from django.db import models
from django.contrib.auth.models import User

class doctorsignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.full_name

class patientsignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.Name
