from django.urls import path
from .views import somePage

urlpatterns = [
    path('', somePage),
]