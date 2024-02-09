
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
<form method="post" action="{% url 'recipes_create' %}" enctype="multipart/form-data">{% csrf_token %}<label for="title">Name:</label>
<input type="text" name="title" id="title">
<br>
<label for="images">images:</label>
<input type="file" name="images" id="images" />
<br>
<label for="description_at">Description:</label>
<textarea name="description_at" id="description_at"></textarea>
<br>
<label for="tkeywords_at">keywords_at:</label>
<input type="text" name="keywords_at" id="keywords_at">
<br />
<div id="group-container"></div>
<button type="button" id="add-group">Add Group</button>
<br>
<input type="submit" value="Submit">
</form>
</div>
</div>
    </div>
  </div>
</div>{% endblock %}