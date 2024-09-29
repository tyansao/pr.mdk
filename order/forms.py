from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_email']