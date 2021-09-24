from django.contrib import admin

from .models import Author, BlogPost

admin.register(Author)
admin.register(BlogPost)
