# Generated by Django 5.0.1 on 2024-01-25 21:40

import django.db.models.deletion
import django.utils.timezone
import modules.recipe.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
                ('description_at', models.CharField(default='', max_length=150, verbose_name='Description')),
                ('keywords_at', models.CharField(default='', max_length=150, verbose_name='Keywords')),
                ('title', models.CharField(default='', max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('status', models.CharField(choices=[('published', 'Опубликовано'), ('draft', 'На модерации')], default='draft', max_length=10, verbose_name='Статус рецепта')),
                ('images', models.FileField(blank=True, default='images/no-images.jpg', null=True, upload_to=modules.recipe.models.get_file_path, verbose_name='Превью рецепта')),
                ('author', models.ForeignKey(default='', editable=False, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='author_posts', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
                'db_table': 'app_recipes',
                'ordering': ['-id'],
            },
        ),
    ]
