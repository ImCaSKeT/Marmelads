# Generated by Django 5.0.1 on 2024-01-25 21:47

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade', '0001_initial'),
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Группа ингридеентов')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test2', to='recipe.recipe')),
            ],
            options={
                'verbose_name': 'Группа ингридеентов',
                'verbose_name_plural': 'Группа ингридеентов',
            },
        ),
        migrations.CreateModel(
            name='IngredientQuantityGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=255, verbose_name='Ингредиент')),
                ('amount', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Мин. количество ингредиентов 1')], verbose_name='Количество')),
                ('measurement_unit', models.CharField(max_length=200, null=True, verbose_name='Мера веса/объема')),
                ('description', models.TextField(blank=True, default='', verbose_name='Примечание')),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test1', to='recipe.ingredientgroup')),
            ],
            options={
                'verbose_name': 'Название ингридеентов',
                'verbose_name_plural': 'Название ингридеентов',
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Мин. количество ингридиентов 1')], verbose_name='Количество')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='grade.ingredient', verbose_name='Ингридиент')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to='recipe.recipe')),
            ],
            options={
                'verbose_name': 'Количество ингредиента',
                'verbose_name_plural': 'Количество ингредиентов',
                'db_table': 'app_recipes_quantity',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipe.RecipeIngredient', to='grade.ingredient'),
        ),
        migrations.AddConstraint(
            model_name='recipeingredient',
            constraint=models.UniqueConstraint(fields=('recipe', 'ingredient'), name='unique ingredient'),
        ),
    ]
