from django.contrib import admin
from src.apps.blog.utils import display_image
from src.apps.blog.models import (
    Post,
    Comment,
    Category,
    Tag
)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """ Административный интерфейс для модели Тег. """

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
        'author__username',
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
        """ Переопределенный метод save_model для автоматической установки автора. """

        obj.author = request.user
        super().save_model(request, obj, form, change)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """ Административный интерфейс для модели Категория. """

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
        'description',
        'author',
        'created_at',
        'updated_at',
    )
    search_fields = (
        'title',
        'slug',
        'author__username',
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
        """ Переопределенный метод save_model для автоматической установки автора. """

        obj.author = request.user
        super().save_model(request, obj, form, change)


class CommentInline(admin.TabularInline):
    """ Inline-класс для комментариев, используемый в административном интерфейсе. """

    model = Comment
    max_num = 0
    extra = 0
    can_delete = False
    fields = (
        'author',
        'text',
        'created_at',
    )
    readonly_fields = (
        'author',
        'text',
        'created_at',
    )
    classes = (
        'collapse',
    )


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """ Административный интерфейс для модели Пост. """

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
        ('Основное', {'fields': ('title', 'slug', 'description')}),
        ('Связи', {'fields': ('category', 'tags', 'author')}),
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
        'author',
        'created_at',
        'updated_at',
    )
    prepopulated_fields = {
        'slug': ('title',)
    }
    inlines = (
        CommentInline,
    )

    def get_queryset(self, request):
        return Post.objects.filter(author=request.user)

    def save_model(self, request, obj, form, change):
        """ Переопределенный метод save_model для автоматической установки автора. """

        obj.author = request.user
        super().save_model(request, obj, form, change)

    def show_list_image(self, obj):
        return display_image(obj, 65, 65)

    def show_detail_image(self, obj):
        return display_image(obj, 150, 150)

    show_list_image.short_description = 'Изображения'
    show_detail_image.short_description = 'Изображения'


