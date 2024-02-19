from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import ForeignKey
from django_ckeditor_5.fields import CKEditor5Field

from django.core import validators
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.urls import reverse

#from django.core.files import ContentFile


#from sorl.thumbnail import ImageField, get_thumbnail


from services.validators import validate_file_extension
from services import DataMixins
from modules.grade.models import Group, Ingredient, Nationality

User = get_user_model()

import os
import uuid


""" Указываем путь куда будут загружаться превью рецептов """
def get_file_path(instance, filename):

    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/thumbnails/', filename)



""" Модель для рецептов """
class Recipe(DataMixins.DataMixin, models.Model):
    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'На модерации')
    )
    difficulty = (
        ('легкая', 'легкая сложность'),
        ('средняя', 'средняя сложность'),
        ('тяжелая', 'тяжелая сложность')
    )
    COOCKING_TIME = (
        ('часов', 'часов'),
        ('минут', 'минут')
    )
    status = models.CharField(choices=STATUS_OPTIONS, default='draft', verbose_name='Статус рецепта', max_length=10)
    images = models.FileField(upload_to=get_file_path, null=True, blank=True, verbose_name='Превью рецепта', default='images/no-images.jpg', validators=[validate_file_extension], )
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_DEFAULT, related_name='author_posts', default='', editable=False, )
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')
    servings = models.PositiveSmallIntegerField(default=1, validators=(
        validators.MinValueValidator(1, message='Мин. количество порций 1'),), verbose_name='Количество порций', )
    cooking = models.CharField(verbose_name='Время готовки', max_length=4, default='')
    cooking_time = models.CharField(choices=COOCKING_TIME, default='hours', verbose_name='минут/часов', max_length=10)
    difficulty = models.CharField(choices=difficulty, default='hours', verbose_name='Сложность рецепта', max_length=10)
    description = CKEditor5Field(config_name='extends', verbose_name='Описание блюда', default='')


    class Meta:
        db_table = 'app_recipes' # Название таблицы в БД
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['-id']

    def get_absolute_url(self):
        return reverse('recipes_detail', kwargs={'slug': self.slug})

    def __repr__(self):
        return 'image(%s, %s)' % (self.title, self.images)


""" Удаляем картинку при изменении фото у рецепта """
@receiver(models.signals.pre_save, sender=Recipe)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_images = Recipe.objects.get(pk=instance.pk).images
        except Recipe.DoesNotExist:
            return
        else:
            new_images = instance.images
            if old_images and old_images.url != new_images.url:
                old_images.delete(save=False)

""" Удаляем картинку при удалении рецепта """
@receiver(pre_delete, sender=Recipe)
def images_recipe_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.images.delete(False)



""" Модель для колличества ингредеентов в рецепте """
class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='ingredient',verbose_name='Ингридиент', )
    amount = models.PositiveSmallIntegerField(default=1,
                                              validators=(validators.MinValueValidator(1,
                                              message='Мин. количество ингридиентов 1'),),
                                              verbose_name='Количество', )

    class Meta:
        db_table = 'app_recipes_quantity'  # Название таблицы в БД
        verbose_name = 'Количество ингредиента'
        verbose_name_plural = 'Количество ингредиентов'
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'ingredient'],
                name='unique ingredient')]




class IngredientGroup(models.Model): # бывший test2
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='test2')
    title = models.CharField(verbose_name='Группа ингридеентов', max_length=255)

    class Meta:
        verbose_name = 'Группа ингридеентов'
        verbose_name_plural = 'Группа ингридеентов'


class IngredientQuantityGroup(models.Model): # бывший test1
    test = models.ForeignKey(IngredientGroup, on_delete=models.CASCADE, related_name='test1')
    ingredient = models.CharField(max_length=255, verbose_name='Ингредиент', )
    amount = models.PositiveSmallIntegerField(default=1, validators=(
        validators.MinValueValidator(1, message='Мин. количество ингредиентов 1'),), verbose_name='Количество', )
    measurement_unit = models.CharField('Мера веса/объема', null=True, max_length=200)
    description = models.TextField(verbose_name='Примечание', default='', blank=True)

    class Meta:
        verbose_name = 'Название ингридеентов'
        verbose_name_plural = 'Название ингридеентов'