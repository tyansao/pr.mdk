from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Book, Clothes


def index(request):
    return render(request, 'home.html')

def showProducts(request):
    clothes = Clothes.objects.all()
    return render(request, 'clothes/products.html', {
        'clothes': clothes,
    })

def showAbout(request):
    return render(request, 'about.html')

def getBook(request):
    books = Book.objects.all()
    return render(request, 'book.html', {
        'books' : books,
    })