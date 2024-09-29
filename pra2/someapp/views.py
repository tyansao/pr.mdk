from django.shortcuts import render

def index(request):
    return render(request, 
                  'index.html', 
                  {
                      'title': 'main page',
                      'content': 'site under construction',
                  })
