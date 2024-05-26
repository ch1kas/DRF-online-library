from django.contrib import admin
from .models import Author, Genre, Book, Comment, Rating, Favorite

admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(Favorite)