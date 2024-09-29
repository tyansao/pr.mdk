from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 100)
    price = models.IntegerField(null = True)
    image = models.ImageField(upload_to = 'book/%Y/%m/%d')