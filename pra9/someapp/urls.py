from django.urls import path
from .views import index, getBookDetail

urlpatterns = [
    path('', index, name = 'mainPage'),
    path('book/<int:id>', getBookDetail, name = 'bookDetail')
]