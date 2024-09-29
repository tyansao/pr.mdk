from django.db import models
from .Course import Course

class Student(models.Model):
    name = models.CharField(max_length = 100)
    second_name = models.CharField(max_length = 100)
    course = models.ForeignKey(Course, on_delete = models.CASCADE, null = True)
