from django.db import models

class Book(models.Model):
    image = models.ImageField(upload_to = 'book/%Y/%m/%d')