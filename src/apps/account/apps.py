from django.apps import AppConfig


class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'src.apps.account'
    verbose_name = 'Аккаунты'

    def ready(self):
        from . import signals