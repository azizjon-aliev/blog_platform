from django.db import models
from src.utils.base.models import Timestampble


class Tag(Timestampble):
    """ Model tag for model post """

    title = models.CharField(verbose_name="Названия", max_length=200, unique=True)
    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(Timestampble):
    """ Model category for model post """

    title = models.CharField(verbose_name="Названия", max_length=200)
    slug = models.SlugField(verbose_name="URL", unique=True)
    description = models.TextField(verbose_name="Описания", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Comment(Timestampble):
    """ Model comment for model post """
    post = models.ForeignKey('Post', verbose_name="Публикация", on_delete=models.CASCADE)
    text = models.TextField(verbose_name="Комментария")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Комментария"
        verbose_name_plural = "Комментарии"


class Post(Timestampble):
    """ Model post for model user """

    image = models.ImageField(verbose_name="Изображения", upload_to="blog/post/images/", blank=True, null=True)
    title = models.CharField(verbose_name="Названия", max_length=200)
    description = models.TextField(verbose_name="Описания", blank=True)
    slug = models.SlugField(verbose_name="URL", unique=True)
    is_published = models.BooleanField(verbose_name="Опубликовать", default=True)
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, verbose_name="Теги", related_name='tags')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
