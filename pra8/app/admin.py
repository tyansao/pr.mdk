from django.contrib import admin
from .models import Book, Clothes

# Register your models here.

@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    pass

@admin.register(Clothes)
class AdminClothes(admin.ModelAdmin):
    pass