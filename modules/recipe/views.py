from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView


from modules.recipe.models import Recipe
from .forms import RecipeCreateForm



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




""" Представление: создание материалов на сайте """
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