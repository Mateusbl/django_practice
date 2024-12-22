from django.contrib import admin
from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    admin.site.register(Category)


class RecipeAdmin(admin.ModelAdmin):
    admin.site.register(Recipe)

# Register your models here.
