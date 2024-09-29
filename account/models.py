from django.db import models
from django.contrib.auth.models import User

class Gender(models.TextChoices):
    MEN = "male"
    WOMEN = "female"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    gender = models.CharField(choices=Gender, blank= True, max_length=6)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    street = models.CharField(max_length=100, blank=True)
    building = models.CharField(max_length=100, blank=True)
    appartmentNumber = models.CharField(max_length=100, blank=True)