from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass
