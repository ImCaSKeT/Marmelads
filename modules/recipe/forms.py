
from django import forms
from .models import Recipe, IngredientGroup, IngredientQuantityGroup

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'images', 'servings', 'cooking', 'cooking_time', 'difficulty', 'description']

class IngredientQuantityGroupForm(forms.ModelForm):
    class Meta:
        model = IngredientQuantityGroup
        fields = ['ingredient', 'amount', 'measurement_unit', 'description']

IngredientQuantityGroupFormSet = forms.inlineformset_factory(
    parent_model=IngredientGroup,
    model=IngredientQuantityGroup,
    form=IngredientQuantityGroupForm,
    extra=1,
    can_delete=True
)

class IngredientGroupForm(forms.ModelForm):
    class Meta:
        model = IngredientGroup
        fields = ['title']

IngredientGroupFormSet = forms.inlineformset_factory(
    parent_model=Recipe,
    model=IngredientGroup,
    form=IngredientGroupForm,
    extra=1,
    can_delete=True
)




"""
    from django import forms
    from .models import Recipe, IngredientGroup, IngredientQuantityGroup, Ingredient

    #Форма добавления статей на сайте

    class RecipeCreateForm(forms.ModelForm):
        ingredient_groups = forms.CharField(label='Группы ингредиентов', required=False)
        ingredient_quantities = forms.CharField(
            label='Ингредиенты в группах (формат: Группа:Ингредиент:Количество:Мера:Примечание)', required=False)

        class Meta:
            model = Recipe
            fields = ('title', 'images', 'description', 'description_at', 'difficulty', 'servings', 'cooking', 'cooking_time', 'keywords_at', )

        def __init__(self, *args, **kwargs):
            # Обновление стилей формы под Bootstrap
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({'class': 'form-control', 'autocomplete': 'off'})
                self.fields['description_at'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
                self.fields['description'].widget.attrs.update({'class': 'form-control django_ckeditor_5'})
                self.fields['description_at'].required = False
                self.fields['description'].required = False




        def save(self, commit=True):
            recipe = super(RecipeCreateForm, self).save(commit=False)
            if commit:
                recipe.save()

            # Обработка создания групп ингредиентов
            ingredient_groups_data = self.cleaned_data.get('test1')
            if ingredient_groups_data:
                group_titles = ingredient_groups_data.split(',')
                for title in group_titles:
                    group = IngredientGroup.objects.create(recipe=recipe, title=title.strip())

            # Обработка добавления ингредиентов в группы
            ingredient_quantities_data = self.cleaned_data.get('test2')
            if ingredient_quantities_data:
                entries = ingredient_quantities_data.split(',')
                for entry in entries:
                    group_title, ingredient_title, amount, measurement_unit, description = entry.split(':')
                    group = IngredientGroup.objects.get(recipe=recipe, title=group_title.strip())
                    ingredient = Ingredient.objects.get(title=ingredient_title.strip())
                    IngredientQuantityGroup.objects.create(group=group, ingredient=ingredient, amount=amount,
                                                           measurement_unit=measurement_unit, description=description)

            return recipe

"""