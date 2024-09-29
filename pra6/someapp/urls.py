from django.urls import path
from .views import getInfo, getAuthor, getAuthorNoPushkin_lmao, getPublisher

urlpatterns = [
    path('', getInfo),
    path('author/pushkin/', getAuthor),
    path('author/some_author/', getAuthorNoPushkin_lmao),
    path('publisher/', getPublisher),
]