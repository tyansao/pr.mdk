from django.urls import path
from .views import index, showProducts, showAbout

urlpatterns = [
    path('', index),
    path('products/', showProducts),
    path('about/', showAbout),
]