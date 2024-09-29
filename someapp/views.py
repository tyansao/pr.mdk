from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Book
from django.db.models import Q

def index(request):
    books = Book.objects.all()
    return render(request, 'books.html', {
        'books': books,
    })

def getBookDetail(request, id):
    book = Book.objects.get(id = id)
    return render(request, 'detail_book.html', {
        'book': book,
    })

def searchBook(request):
    if request.method == 'GET' and request.GET['search']:
        search = request.GET['search']
        books = Book.objects.filter(
            Q(title__icontains = search)
        )
        return render(request, "books.html", {
            'books' : books,
        })
    return redirect('mainPage')