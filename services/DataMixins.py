"""
Этот файл содержит методы и поля для всех моделей, которые наследуются от
класса ***Mixin, обеспечивая их данными записи.

"""
from django.db import models
from django.utils.timezone import now


""" Добавляем поля создание и обновления модели """
class DataMixin(models.Model):
    created_at = models.DateTimeField(default=now, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    description_at = models.CharField(max_length=150, verbose_name='Description', default='',)
    keywords_at = models.CharField(max_length=150, verbose_name='Keywords', default='',)
    title = models.CharField(max_length=255, verbose_name='Заголовок', default='')
    slug = models.SlugField(unique=True, max_length=50, db_index=True, null=False, blank=False, verbose_name='Ссылка')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title