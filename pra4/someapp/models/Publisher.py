from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length = 100)
    established = models.DateField()