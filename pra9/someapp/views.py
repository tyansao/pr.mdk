from django.shortcuts import render
from .models import Book

# Create your views here.

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