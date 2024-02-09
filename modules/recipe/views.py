from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView


from modules.recipe.models import Recipe
from .forms import RecipeForm, IngredientGroupFormSet, RecipeIngredientFormSet

# Create your views here.

"""  Главная страница сайта  """
class RecipeListView(ListView):
    template_name = 'home.tpl'
    model = Recipe
    context_object_name = 'recipes'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['articles'] = Article.objects.all()[:6]
        #context['categores'] = Category.objects.all()[:5]
        #context['cats'] = Category.objects.all()
        context['title'] = f'Заголовок страницы если нет возможности сделать title '
        context['description_at'] = f'Короткое описание страницы'
        """ Выводим общие число опубликованных рецептов """
        context['count'] = Recipe.objects.all().filter(status='published').count()
        """ Выводим последние опубликованные 6 рецептов """
        context['recipes'] = Recipe.objects.all().filter(status='published')[:6]
        return context

    def get_queryset(self):
        queryset = Recipe.objects.all()[:6]
        return queryset



class RecipesDetailView(DetailView):
    model = Recipe
    template_name = 'modules/recipe/fullstory.tpl'
    context_object_name = 'recipes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.title
        return context




""" Представление: создание материалов на сайте
class RecipeCreateView(CreateView):
    model = Recipe
    template_name = 'modules/recipes/recipe_create.tpl'
    form_class = RecipeCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи на сайт'
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return super().form_valid(form)
 """

# Версия 2
class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'modules/recipes/recipe_create.tpl'
    success_url = '/'

    def get_context_data(self, **kwargs):

        data = super().get_context_data(**kwargs)
        data['title'] = 'Добавление статьи на сайт'

        if self.request.POST:
            data['ingredient_group_formset'] = IngredientGroupFormSet(self.request.POST)
            data['recipe_ingredient_formset'] = RecipeIngredientFormSet(self.request.POST)
        else:
            data['ingredient_group_formset'] = IngredientGroupFormSet()
            data['recipe_ingredient_formset'] = RecipeIngredientFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        ingredient_group_formset = context['ingredient_group_formset']
        recipe_ingredient_formset = context['recipe_ingredient_formset']
        if ingredient_group_formset.is_valid() and recipe_ingredient_formset.is_valid():
            self.object = form.save()
            ingredient_group_formset.instance = self.object
            ingredient_group_formset.save()
            recipe_ingredient_formset.instance = self.object
            recipe_ingredient_formset.save()
            return super().form_valid(form)
        else:
            return self.form_invalid(form)