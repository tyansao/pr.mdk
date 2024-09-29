from django.contrib import admin
from someapp.models import Author, Book, Publisher

@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    pass

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass

@admin.register(Publisher)
class AdminPublisher(admin.ModelAdmin):
    pass