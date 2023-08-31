from django.db import models
from src.utils.base.models import Timestampble


class Tag(Timestampble):
    """ Model tag for model post """

    title = models.CharField(verbose_name="Названия", max_length=200)
    slug = models.SlugField(verbose_name="URL", unique=True)

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
