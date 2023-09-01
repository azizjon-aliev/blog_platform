from django.contrib import admin
from .models import (
    Tag,
    Category,
    Post,
    Comment,
)
from .utils import display_image


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ Admin interface for tag model """

    date_hierarchy = "created_at"
    list_display = (
        'title',
        'slug',
        'author',
        'created_at',
    )
    list_filter = (
        'author',
    )
    fields = (
        'title',
        'slug',
        'author',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'title',
        'slug',
    )
    readonly_fields = (
        'author',
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """ Admin interface for comment model """

    date_hierarchy = "created_at"
    autocomplete_fields = (
        'post',
    )
    list_display = (
        'post',
        'text',
        'created_at',
    )
    list_filter = (
        'post',
    )
    search_fields = (
        'post__title',
        'text',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
    )


class CommentInline(admin.TabularInline):
    model = Comment
    max_num = 0
    extra = 0
    can_delete = False
    fields = (
        'text',
        'created_at',
    )
    readonly_fields = (
        'text',
        'created_at',
    )
    classes = (
        'collapse',
    )


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
    inlines = (
        CommentInline,
    )

    def show_list_image(self, obj):
        return display_image(obj, 65, 65)

    def show_detail_image(self, obj):
        return display_image(obj, 150, 150)

    show_list_image.short_description = 'Изображения'
    show_detail_image.short_description = 'Изображения'
