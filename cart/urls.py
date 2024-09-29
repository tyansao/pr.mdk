from django.urls import path
from .views import cart_detail, cart_add, cart_remove, cart_remove_all, cart_add_inCart

urlpatterns = [
    path('', cart_detail, name='cart_detail'),
    path('add/<int:book_id>', cart_add, name='cart_add'),
    path('addic/<int:book_id>', cart_add_inCart, name='cart_addic'),
    path('rem/<int:book_id>', cart_remove, name='cart_remove'),
    path('remall/<int:book_id>', cart_remove_all, name='cart_remove_all'),

]