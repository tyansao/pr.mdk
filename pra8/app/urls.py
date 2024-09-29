from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.showProducts, name='showProds'),
    path('about/', views.showAbout, name='showAbou'),
    path('book/', views.getBook, name='showBook'),
]