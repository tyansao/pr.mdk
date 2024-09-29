from django.shortcuts import render
from .cart import CartSession
from django.http import  HttpRequest
from someapp.models import Book
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

def cart_add(request: HttpRequest, book_id):
    cart = CartSession(request.session)
    book = get_object_or_404(Book, id=book_id)
    cart.add(book=book)

    return redirect('bookDetail', book_id)

# костыли, знаю :(
def cart_add_inCart(request: HttpRequest, book_id):
    cart = CartSession(request.session)
    book = get_object_or_404(Book, id=book_id)
    cart.add(book=book)

    return redirect(reverse('cart_detail'))

def cart_remove(request: HttpRequest, book_id):
    cart = CartSession(request.session)
    book = get_object_or_404(Book, id=book_id)
    cart.remove(book=book)

    return redirect(reverse('cart_detail'))

def cart_remove_all(request: HttpRequest, book_id):
    cart = CartSession(request.session)
    book = get_object_or_404(Book, id=book_id)
    cart.remove_all(book=book)

    return redirect(reverse('cart_detail'))

def cart_detail(request: HttpRequest):
    cart = CartSession(request.session)
    return render(request, 'cart_detail.html', {
        'cart': cart
    })
