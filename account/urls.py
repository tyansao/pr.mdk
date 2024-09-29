from django.urls import path
from .views import register, loginUser, logoutUser, profileView, profileEdit

urlpatterns = [
    path('register/', register, name = 'register'),
    path('login/', loginUser, name = 'login'),
    path('logout/', logoutUser, name = 'logout'),
    path('', profileView, name = 'account'),
    path('edit/', profileEdit, name = 'edit'),
]
