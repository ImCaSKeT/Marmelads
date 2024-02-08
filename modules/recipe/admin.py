from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.forms import TextInput, Textarea
import nested_admin

from .models import (Recipe, RecipeIngredient, IngredientGroup, IngredientQuantityGroup)


class RecipeIngredientAdmin(nested_admin.NestedStackedInline):
    extra = 1
    model = RecipeIngredient
    autocomplete_fields = ('ingredient',)


class IngredientQuantityGroupAdmin(nested_admin.NestedStackedInline):
    extra = 1
    model = IngredientQuantityGroup
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': [('ingredient',), ('amount', 'measurement_unit',), 'description', ]
        }),
    ]
    classes = ('collapse',)


class IngredientGroupAdmin(nested_admin.NestedStackedInline):
    extra = 1
    model = IngredientGroup
    inlines = [IngredientQuantityGroupAdmin]
    classes = ('collapse',)



@admin.register(Recipe)
class RecipeAdmin(nested_admin.NestedModelAdmin):
    save_on_top = True
    model = Recipe
    inlines = [IngredientGroupAdmin]
    list_filter = ('status', 'created_at',)
    list_display = ('id', 'title', 'post_photo', 'status', 'customer_link', 'created_at', 'updated_at')
    list_display_links = ['id', 'title']
    list_editable = ['status']
    date_hierarchy = 'created_at'
    prepopulated_fields = {'slug': ('title',)}


    fieldsets = [
        ("Основная информация", {
            'classes': ('suit-tab suit-tab-general',),
            'fields': [('title', 'slug'), ('images')]
        }),
        ("Дата создания", {
            'classes': ('suit-tab suit-tab-general',),
            'fields': [('created_at') ]
        }),
        ("SEO данные", {
            'classes': ('suit-tab suit-tab-general',),
            'fields': [('description_at', 'keywords_at') ]
        }),
        ("Для админов", {
            'classes': ('suit-tab suit-tab-general',),
            'fields': [('status') ]
        }),
    ]

    """ Выводим ссылку на автора рецепта """
    @admin.display(description="Автор рецепта")
    def customer_link(self, obj):
        if obj.author:
            return format_html("<a href='{0}'>{1}</a>".format(
                reverse('admin:auth_user_change',
                        args=(obj.author.pk,)),
                obj.author)
            )

    """ Автоматический подставляем автора к создаваемому рецепту """
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        super(RecipeAdmin, self).save_model(request=request, obj=obj, form=form, change=change)

    """ Выводим миниатюру рецепта """
    @admin.display(description="Изображение")
    def post_photo(self, recipe: Recipe):
        return format_html(f""
                           f"<div syle='width: 45px; height: 45px; position: relative;'>"
                           f"<img src='{recipe.images.url}' style='object-fit: cover; width: 45px; height: 45px; border-radius: 16px;'  >"
                           f"</div>")