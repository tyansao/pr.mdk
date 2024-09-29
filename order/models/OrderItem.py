from django.db import models
from django.contrib.auth.models import User
from someapp.models import Book
from .Order import Order

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.book} for {self.order}"