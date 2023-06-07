from django.contrib import admin
from making_queries.models import Blog, Author, Entry


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline']


@admin.register(Author)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

@admin.register(Entry)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['headline',  'body_text', 'pub_date', 'blog', 'mod_date', 'number_of_comments', 'number_of_pingbacks', 'rating']