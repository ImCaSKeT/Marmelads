{% load static %}<!DOCTYPE html>
<html lang="ru">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Marmelads.ru</title>
    <meta name="description" content="{{ description_at }}">
    <meta property="og:site_name" content="Кулинарное путешествие: рецепты со всего мира и домашние хитрости приготовления еды">
    <meta property="og:type" content="article">
    <meta property="og:title" content="{{ title }}">
    <meta property="og:url" content="{{ request.get_full_path }}">
    <meta property="og:image" content="{% if images %}{{ images }}{% else %}{% static 'images/home_images.jpg' %}{% endif %}">
    <meta property="og:description" content="{{ description_at }}">
    <link rel="canonical" href="{{ request.get_full_path }}">
    <link rel="shortcut icon" href="{% static 'images/favicon.png' %}">
    <link rel="stylesheet" href="{% static 'styles/fontawesome.min.css' %}">
    <link rel="stylesheet" href="{% static 'styles/all.min.css' %}">
    <link rel="stylesheet" href="{% static 'styles/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'styles/styleshet.min.css' %}">
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script>
      $(document).ready(function() {
          var groupCounter = 0;
      
          $('#add-group').click(function() {
              groupCounter++;
              var groupDiv = $('<div>').addClass('group');
              var groupNameInput = $('<input>').attr('type', 'text').attr('name', 'group-' + groupCounter + '-name');
              var addIngredientButton = $('<button>').attr('type', 'button').text('Add Ingredient');
              var ingredientList = $('<ul>').addClass('ingredient-list');
      
              addIngredientButton.click(function() {
                  var ingredientInput = $('<input>').attr('type', 'text').attr('name', 'group-' + groupCounter + '-ingredient');
                  var listItem = $('<li>').append(ingredientInput);
                  ingredientList.append(listItem);
              });
      
              groupDiv.append($('<label>').text('Group Name:')).append(groupNameInput);
              groupDiv.append(addIngredientButton);
              groupDiv.append(ingredientList);
              $('#group-container').append(groupDiv);
          });
      });
    </script>
  </head>
  <body>
     {% block header %}
    <h1 class="title">HEADER</h1>{% endblock %}
    {% block banner %}
    <h2 class="title">BANNER</h2><span>тут будет поиск</span><br><span>Всего опубликованно {{ count }} рецепта</span>{% endblock %}
    {% block home_recipe %}
    {% endblock %}
    {% block content %}
    {% endblock %}
    <script src="{% static 'js/popper.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
    <script src="{% static 'js/core.js' %}"></script>
  </body>
</html>