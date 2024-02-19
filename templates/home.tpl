
{% extends 'core.tpl' %}
{% block home_recipe %}
<div class="container"> 
  <div class="row"> 
    <div class="col-sm-3">
       {% if user.is_authenticated %}<span>авторизован </span><a href="{% url 'recipes_create' %}">Добавить рецепт</a>{% else %}<span>не авторизован</span><a href="{% url 'recipes_create' %}">Добавить рецепт</a>{% endif %}</div>
    <div class="col-sm-9"> 
      <div class="row">  {% for r in recipes %}
        <article class="shortstory col-sm-4">
          <div class="rtin-single-post">
            <div class="rtin-img"><img class="post-image" src="{{ r.images.url }}" alt="{{ r.title }}"/>
              <div class="dropdown"><a class="edit_link" id="dropEdit" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false"><i class="fa-regular fa-ellipsis"></i></a>
                <ul class="dropdown-menu" aria-labelledby="dropEdit">{% if r.author == request.user %}
                  <li class="dropdown-item"><a href="/">Добавить в книгу</a></li>
                  <li class="dropdown-item"><a href="/">Пожаловаться</a></li>
                  <li class="dropdown-item"><a href="/">Редактировать</a></li>
                  <li class="dropdown-item"><a href="/">Удалить</a></li>{% elif request.user.is_superuser %}
                  <li class="dropdown-item"><a href="/">Добавить в книгу</a></li>
                  <li class="dropdown-item"><a href="/">Пожаловаться</a></li>
                  <li class="dropdown-item"><a href="/">Редактировать</a></li>
                  <li class="dropdown-item"><a href="/">Удалить</a></li>{% else %}
                  <li class="dropdown-item"><a href="/">Добавить в книгу</a></li>
                  <li class="dropdown-item"><a href="/">Пожаловаться</a></li>{% endif %}
                </ul>
              </div>
            </div><a href="{% url 'recipes_detail' r.slug %}">{{ r.title }}</a>
          </div>
        </article>  {% endfor %}
      </div>
    </div>
  </div>
</div>{% endblock %}