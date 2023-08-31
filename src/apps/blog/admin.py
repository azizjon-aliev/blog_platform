from django.contrib import admin
from django.utils.html import format_html

from .models import (
    Tag,
    Category,
    Post,
)
from .utils import display_image


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ Admin interface for tag model """

    date_hierarchy = "created_at"
    list_display = (
        'title',
        'slug',
        'created_at',
    )
    search_fields = (
        'title',
        'slug',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Admin interface for category model """

    date_hierarchy = "created_at"
    list_display = (
        'title',
        'slug',
        'created_at',
    )
    search_fields = (
        'title',
        'slug',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(Post)
class PostyAdmin(admin.ModelAdmin):
    """ Admin interface for post model """

    date_hierarchy = "created_at"
    autocomplete_fields = (
        'category',
        'tags',
    )
    list_display = (
        'show_list_image',
        'title',
        'category',
        'is_published',
        'created_at',
    )
    list_filter = (
        'is_published',
        'category',
        'tags',
    )
    fieldsets = (
        ('Медиа', {'fields': ('show_detail_image', 'image')}),
        ('Основнее', {'fields': ('title', 'slug', 'description')}),
        ('Связи', {'fields': ('category', 'tags')}),
        ('Дата и время', {'fields': ('created_at', 'updated_at')}),
    )
    search_fields = (
        'title',
        'slug',
        'category__title',
        'tags__title',
    )
    readonly_fields = (
        'show_detail_image',
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }

    def show_list_image(self, obj):
        return display_image(obj, 65, 65)

    def show_detail_image(self, obj):
        return display_image(obj, 150, 150)

    show_list_image.short_description = 'Изображения'
    show_detail_image.short_description = 'Изображения'
