
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    cin = models.CharField(max_length=10)
    gender = models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.username