
{% extends 'core.tpl' %}
{% block content %}
<div class="container">
  <div class="row"> 
    <div class="col-sm-9">
      <article id="RecipePost">
        <ul class="entry-meta">
          <li class="single-meta"><i class="fa-regular fa-calendar-days"></i>{{ recipe.created_at|date:"d.m.Y" }}</li>
          <li class="single-meta"><i class="fa-regular fa-user-chef"></i><a href="/">
               {% if recipe.author.profile.user.first_name %}
              		{{ recipe.author.profile.user.first_name }}
              {% else %}
              		{{ recipe.author }}
              {% endif %}</a></li>
        </ul>
        <ul class="entry-meta">
          <li class="single-meta"><i class="fa-regular fa-tags"></i><a href="/">Салаты {{ recipe.category.title }} </a>/ <a href="/">Закуски {{ recipe.group.title }}</a></li>
          <li class="single-meta"><i class="fa-sharp fa-regular fa-book"></i><span>Американская кухня {{ recipe.nationality }}</span></li>
          <li class="single-meta"><i class="fa-regular fa-signal"></i><span>{{ recipe.difficulty }}</span></li>
        </ul>
        <div class="item-figure"><img class="post-image" src="{{ recipe.images.url }}" alt="{{ recipe.title }}"/></div>
        <div class="item-feature">
          <ul class="feature_list">
            <li class="feature_item">
              <div class="feature-wrap">
                <div class="media">
                  <div class="feature-icon"><i class="fa-regular fa-timer"></i></div>
                  <div class="media-body">
                    <div class="feature-title">Время</div>
                    <div class="feature-sub-title">{{ recipe.cooking }} {{ recipe.cooking_time }}</div>
                  </div>
                </div>
              </div>
            </li>
            <li class="feature_item">
              <div class="feature-wrap">
                <div class="media">
                  <div class="feature-icon"><i class="fa-sharp fa-regular fa-bowl-food"></i></div>
                  <div class="media-body">
                    <div class="feature-title">Порций</div>
                    <div class="feature-sub-title">{{ recipe.servings }}</div>
                  </div>
                </div>
              </div>
            </li>
            <li class="feature_item">
              <div class="feature-wrap">
                <div class="media">
                  <div class="feature-icon"><i class="fa-regular fa-signal"></i></div>
                  <div class="media-body">
                    <div class="feature-title">Сложность</div>
                    <div class="feature-sub-title">{{ recipe.difficulty }}</div>
                  </div>
                </div>
              </div>
            </li>
            <li class="feature_item">
              <div class="feature-wrap">
                <div class="media">
                  <div class="feature-icon"><i class="fa-regular fa-eye"></i></div>
                  <div class="media-body">
                    <div class="feature-title">Просмотров</div>
                    <div class="feature-sub-title">{{ recipe.get_view_count }}</div>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </div>{{ recipe.description|safe }}
        <div class="row"> 
          <div class="col-sm-6">
             {{ recipe.description|safe }}</div>
          <div class="col-sm-6"> 
            <div class="ingridients-wrap">{% for ing in recipe.test2.all %}
              <h5 class="item-title"> <i class="fa-regular fa-list-check"></i><span>{{ ing.title }}</span></h5>
              <ul class="ingredient-list">{% for nm in ing.test1.all %}
                <li class="item_list d-flex"> </li><span class="me-auto">{{ nm.ingredient }}</span><span>{{ nm.amount }} {{ nm.measurement_unit }} </span>{% endfor %}
              </ul>{% endfor %}
            </div>
          </div>
        </div>
      </article>
    </div>
    <div class="col-sm-3"></div>
  </div>
</div>{% endblock %}