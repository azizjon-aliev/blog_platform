from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """ Custom user class for Django """

    email = models.EmailField(verbose_name="Email", unique=True, db_index=True)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
