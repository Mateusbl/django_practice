from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(
        max_length=45,
        verbose_name='Category Name',
        help_text='Enter the category name'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['title']


class Recipe(models.Model):
    title = models.CharField(
        max_length=65,
        verbose_name='Recipe Title',
        help_text='Enter the recipe title'
    )
    description = models.CharField(
        max_length=165,
        verbose_name='Description',
        help_text='Brief description of the recipe'
    )
    slug = models.SlugField(
        unique=True,
        help_text='URL-friendly version of the recipe title'
    )
    preparation_time = models.IntegerField(
        verbose_name='Preparation Time',
        help_text='Time needed to prepare the recipe'
    )
    preparation_time_unit = models.CharField(
        max_length=10,
        verbose_name='Time Unit',
        help_text='Unit of time (e.g., minutes, hours)'
    )
    servings = models.IntegerField(
        verbose_name='Servings',
        help_text='Number of servings'
    )
    preparation_steps = models.TextField(
        verbose_name='Preparation Steps',
        help_text='Detailed recipe instructions'
    )
    preparation_steps_is_html = models.BooleanField(
        default=False,
        verbose_name='Is HTML',
        help_text='Check if preparation steps contain HTML'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(
        default=False,
        verbose_name='Published',
        help_text='Check to make the recipe public'
    )
    cover = models.ImageField(
        upload_to="recipes/cover/%Y/%m/%d",
        verbose_name='Cover Image'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Category'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Author'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'
        ordering = ['-created_at']