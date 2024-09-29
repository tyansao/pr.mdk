from django.shortcuts import render, HttpResponse

# Create your views here.

def somePage(request):
    return HttpResponse('<h1>hi</h1>')
