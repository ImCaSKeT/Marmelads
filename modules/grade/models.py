from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


""" Модель для Ингредеентов 
class Ingredient(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название ингредиента')

    class Meta:
        ordering = ['title']
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'
        db_table = 'app_grade_ingredient'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title
 """


""" Модель для национальности рецепта """
class Nationality(models.Model):
    title = models.CharField(max_length=150, verbose_name='Национальность')
    slug = models.SlugField(max_length=255, verbose_name='URL группы', blank=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Национальность'
        verbose_name_plural = 'Национальность'
        db_table = 'app_grade_nationality'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('nationality', kwargs={'slug': self.slug})



""" Модель для Группировки рецептов """
class Group(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название группы')
    slug = models.SlugField(max_length=255, verbose_name='URL группы', blank=True)
    #category = ForeignKey(Category, on_delete=models.PROTECT, related_name='categories', default='', verbose_name='Категория')

    class Meta:
        ordering = ['title']
        verbose_name = 'Грцппа рецептов'
        verbose_name_plural = 'Группы рецептов'
        db_table = 'app_grade_groups'

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('group', kwargs={'slug': self.slug})
