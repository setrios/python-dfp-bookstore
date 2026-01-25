from django.contrib import admin
from .models import Book, Review

# Register your models here.

class ReviewInline(admin.TabularInline):  # create inline
    model = Review  

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]  # use inline 
    list_display = ('title', 'author', 'price')

admin.site.register(Book, BookAdmin)