
{% extends 'core.tpl' %}
{% block content %}
<div class="container"> 
  <div class="row"> 
    <div class="col-sm-12">
      <div class="card mb-3 border-0 nth-shadow">
<div class="card-body">
<div class="card-title nth-card-title">
<h4>Добавление статьи</h4>
</div>
<form method="post" action="{% url 'recipes_create' %}" enctype="multipart/form-data">{% csrf_token %}
      {{ form.as_p }}<div class="d-grid gap-2 d-md-block mt-2">
<button type="submit" class="btn btn-dark">Добавить статью</button>
</div>
</form>
</div>
</div>
    </div>
  </div>
</div>{% endblock %}