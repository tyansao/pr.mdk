from django.db import models
from .Teacher import Teacher

class Course(models.Model):
    name = models.CharField(max_length = 100)
    teacher = models.ForeignKey(Teacher, on_delete = models.CASCADE)
