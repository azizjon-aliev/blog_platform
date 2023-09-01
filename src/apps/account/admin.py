from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    CustomUser,
)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            self.fieldsets = (
                (None, {"fields": ("username", "password")}),
                ('Персональная информация', {"fields": ("first_name", "last_name", "email")}),
            )
            return qs.filter(id=request.user.id)
        return qs

    # Ограничиваем права доступа к пользователям
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        if obj is not None and obj == request.user:
            return True
        return False

    # Ограничиваем возможность добавления новых пользователей
    def has_add_permission(self, request):
        return False
