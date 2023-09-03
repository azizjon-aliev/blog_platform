from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ Custom user class for Django """

    email = models.EmailField(
        verbose_name="Email",
        unique=True,
        db_index=True
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Profile(models.Model):
    """ Model profile for model custom user """

    user = models.OneToOneField(
        CustomUser,
        verbose_name="Пользователь",
        on_delete=models.CASCADE
    )
    avatar = models.ImageField(
        verbose_name="Автар",
        upload_to="accounts/profiles/avatars/",
        blank=True,
        null=True
    )
    about = models.TextField(verbose_name="О себе", blank=True)
    address = models.CharField(
        verbose_name="Адрес",
        max_length=225,
        blank=True
    )

    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Время изменения", auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
