from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'home.html')

def showProducts(request):
    return render(request, 'clothes/products.html', {
        'clothes': [ {'name': 'shirt', 
                      'img': 'img/clothes/shirt.webp'}, 
                      {'name': 'hat', 
                      'img': 'img/clothes/hat.webp'},
                      {'name': 'coat', 
                      'img': 'img/clothes/coat.jpg'},
                    ],
    })

def showAbout(request):
    return render(request, 'about.html')