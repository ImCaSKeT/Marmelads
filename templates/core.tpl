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
    <script src="{% static 'js/jquery.min.js' %}"></script>
    <script src="{% static 'js/popper.min.js' %}"></script>
    <script src="{% static 'js/bootstrap.min.js' %}"></script>
    <script src="{% static 'js/core.js' %}"></script>
  </body>
</html>