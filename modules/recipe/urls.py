from django.urls import path

from .views import (RecipeListView, RecipesDetailView, RecipeCreateView,  )
#from modules.user.views import ProfileDetailView




urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('recipe/<str:slug>.html', RecipesDetailView.as_view(), name='recipes_detail'),

    path('recipe/create/', RecipeCreateView.as_view(), name='recipes_create'),

]