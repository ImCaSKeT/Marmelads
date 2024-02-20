
{% extends 'core.tpl' %}
{% block content %}
<div class="container"> 
  <div class="row"> 
    <div class="col-sm-9">
      <div class="card mb-3 border-0 nth-shadow">
<div class="card-body">
<form method="post" action="{% url 'recipes_create' %}" enctype="multipart/form-data">{% csrf_token %}
      {{ form.as_p }}<h2>Ingredient Groups</h2>{{ group_formset.management_form }}<div class="group-form">{% for form in group_formset.forms %}
         {{ form.as_p }}<button class="add-ingredient-btn">Add Ingredient</button>
<div class="ingredient-form">
<input type="text" name="ingredient_name" placeholder="Ingredient Name">
<input type="text" name="quantity" placeholder="Quantity">
</div>{% endfor %}</div>
<button id="add-group-btn">Add Ingredient Group</button>
      <input class="btn_red" type="submit" value="Опубликовать рецепт"/>
    </div>
  </div>
</div>{% endblock %}