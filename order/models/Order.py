from django.db import models
from django.contrib.auth.models import User

class PaymentStatus(models.TextChoices):
    PENDING = "Under consideration"
    PROCESSED = "In processing"
    SHIPPED = "Sent"
    DELIVERED = "Delivered"

class Order(models.Model):
    customer_user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer_email = models.EmailField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=PaymentStatus)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} for {self.customer_user.username}"