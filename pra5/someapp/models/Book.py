from django.db import models
from .Author import Author
from .Publisher import Publisher

class Book(models.Model):
    title = models.CharField(max_length = 100)
    publicationDate = models.DateField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    publishers = models.ManyToManyField(Publisher)