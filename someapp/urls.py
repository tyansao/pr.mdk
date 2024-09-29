from django.urls import path
from .views import index, getBookDetail, searchBook

urlpatterns = [
    path('', index, name = 'mainPage'),
    path('book/<int:id>', getBookDetail, name = 'bookDetail'),
    path('search', searchBook, name = 'search'),
]