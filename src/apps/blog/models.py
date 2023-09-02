from django.contrib.auth import get_user_model
from django.db import models
from src.utils.base.models import (
    Timestampble,
    Authorable,
    Permalinkable
)

User = get_user_model()


class Tag(Timestampble, Permalinkable, Authorable):
    """ Модель тега для постов. """

    title = models.CharField(
        verbose_name="Название",
        max_length=200,
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Category(Timestampble, Permalinkable, Authorable):
    """ Модель категории для постов. """

    title = models.CharField(
        verbose_name="Название",
        max_length=200,
        unique=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Comment(Timestampble, Authorable):
    """ Модель комментария для постов. """

    post = models.ForeignKey(
        'Post',
        verbose_name="Публикация",
        on_delete=models.CASCADE
    )
    text = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        return self.text

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"


class Post(Timestampble, Permalinkable, Authorable):
    """ Модель поста для пользователей. """

    # Блок полей медиа
    image = models.ImageField(
        verbose_name="Изображение",
        upload_to="blog/post/images/",
        blank=True,
        null=True
    )

    # Блок полей основной информации
    title = models.CharField(verbose_name="Заголовок", max_length=200)
    description = models.TextField(verbose_name="Описание", blank=True)
    is_published = models.BooleanField(verbose_name="Опубликован", default=True)
    category = models.ForeignKey(
        Category,
        verbose_name="Категория",
        on_delete=models.CASCADE
    )
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        verbose_name="Теги",
        related_name='posts'
    )

    def __str__(self):
        return self.title

    @property
    def comments_count(self):
        return Comment.objects.filter(post=self).count()

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"


class LikeDislikePost(Timestampble):
    """ Like and dislike post"""

    TYPE_CHOICES = (
        (1, 'Нравится'),
        (2, 'Не нравится'),
    )
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    post = models.ForeignKey(Post, verbose_name="Публикация", on_delete=models.CASCADE)
    type = models.PositiveSmallIntegerField(verbose_name="Тип", choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.post.title}"

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Нравится пост"
        verbose_name_plural = "Нравится посты"
