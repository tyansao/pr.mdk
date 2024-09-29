from django.shortcuts import render # type: ignore

def index(request):
    return render(request, 
                  'index1.html', 
                  {
                      'book_link': 'https://www.litres.ru/book/aleksandr-pushkin/kapitanskaya-dochka-171967/',
                      'book_img': 'https://cdn.litres.ru/pub/c/cover_415/171967.webp',
                  })
