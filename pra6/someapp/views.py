from django.shortcuts import render, HttpResponse
from .models import Book

# Create your views here.

def getInfo(request):
    book = Book.objects.get(id = 1)
    return render(request, 'base.html', {
        'book': book,
    })

def getAuthor(request):
    bookAuthor = Book.objects.filter(author__name = "Pushkin")
    return render(request, 'author.html', {
        'bookAuthor': bookAuthor,
    })

def getAuthorNoPushkin_lmao(request):
    bookAuthor = Book.objects.filter(author__name = "someAuthor")
    return render(request, 'author.html', {
        'bookAuthor': bookAuthor,
    })

def getPublisher(request):
    bookPublisher = Book.objects.filter(publishers__name = "somePublisher")
    return render(request, 'publishers.html', {
        'bookPublisher': bookPublisher,
    })