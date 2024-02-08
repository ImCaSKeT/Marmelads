# Generated by Django 5.0.1 on 2024-01-25 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название группы')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='URL группы')),
            ],
            options={
                'verbose_name': 'Грцппа рецептов',
                'verbose_name_plural': 'Группы рецептов',
                'db_table': 'app_grade_groups',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Название ингредиента')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
                'db_table': 'app_grade_ingredient',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Национальность')),
                ('slug', models.SlugField(blank=True, max_length=255, verbose_name='URL группы')),
            ],
            options={
                'verbose_name': 'Национальность',
                'verbose_name_plural': 'Национальность',
                'db_table': 'app_grade_nationality',
                'ordering': ['title'],
            },
        ),
    ]