from django.contrib import admin

# Register your models here.
from .models import *

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'avatar', 'description']
admin.site.register(UserProfile, UserProfileAdmin)

class ArticleAdmin(admin.ModelAdmin):
    search_field = ['title', 'content']
    list_display = ['title', 'category', 'created_at']

admin.site.register(Article, ArticleAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'cover']

admin.site.register(Category, CategoryAdmin)

