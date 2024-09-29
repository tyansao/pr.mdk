from django.db import models # type: ignore

class Book(models.Model):
    name = models.CharField(max_length = 255)
    author = models.CharField(max_length = 10)
    year = models.DateField(null = True)

class Author(models.Model):
    name = models.CharField(max_length = 100)
    dateOfBirth = models.DateField(null = True)
    gender = models.CharField(max_length = 6)