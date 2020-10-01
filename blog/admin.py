from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'slug', 'pub_date']
    prepopulated_fields = {'slug': ('title',)}  # when a post is created, slug is automatically filled based on title
    search_fields = ['title', 'content']    # provides a search bar for searching database


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'tag']


# Register your models here.
admin.site.register(Author)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
