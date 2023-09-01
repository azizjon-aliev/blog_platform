from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Authorable(models.Model):
    """  Абстрактная модель, которая добавляет поле 'author', представляющее пользователя, создавшего объект. """

    author = models.ForeignKey(User, verbose_name="Автор", on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Permalinkable(models.Model):
    """ Абстрактная модель, которая добавляет поле 'slug' для создания уникальных URL-адресов. """

    slug = models.SlugField(verbose_name="URL", unique=True, db_index=True)

    class Meta:
        abstract = True


class Publishable(models.Model):
    """ Абстрактная модель, которая добавляет поле 'publish_date' для отслеживания даты и времени публикации. """

    publish_date = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Timestampble(models.Model):
    """
    Абстрактная модель,
    которая добавляет поля 'created_at' и 'updated_at' для отслеживания времени создания и изменения объекта.
    """

    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время изменения", auto_now=True)

    class Meta:
        abstract = True
