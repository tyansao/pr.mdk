from django.db import models

class Clothes(models.Model):
    name = models.CharField(max_length = 100)
    cost = models.IntegerField()
    image = models.ImageField(upload_to = 'clothes/%Y/%m/%d')