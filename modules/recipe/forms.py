from django import forms
from .models import Recipe



""" Форма добавления статей на сайте """
class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'slug', 'images', 'ingredients', 'description_at', 'keywords_at')