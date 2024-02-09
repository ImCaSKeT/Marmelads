from django import forms
from .models import Recipe, RecipeIngredient
from ..grade.models import Ingredient, Group

from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, IngredientGroup, RecipeIngredient


class IngredientGroupForm(forms.ModelForm):
    class Meta:
        model = IngredientGroup
        fields = ['title']

IngredientGroupFormSet = inlineformset_factory(
    Recipe,
    IngredientGroup,
    form=IngredientGroupForm,
    extra=1,
    can_delete=True
)

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'amount']

RecipeIngredientFormSet = inlineformset_factory(
    Recipe,
    RecipeIngredient,
    form=RecipeIngredientForm,
    extra=1,
    can_delete=True
)

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'slug', 'images', 'description_at', 'keywords_at']

class IngredientGroupForm(forms.ModelForm):
    class Meta:
        model = IngredientGroup
        fields = ['title']

class RecipeIngredientForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'amount']



""" Форма добавления статей на сайте
class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'slug', 'images', 'ingredients', 'description_at', 'keywords_at')

    name = forms.CharField()
    date = forms.DateInput()
    members = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
     """