from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from src.apps.account.models import Profile

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    """
    Сериализатор для входа.

    Позволяет пользователям войти, предоставив имя пользователя или электронную почту и пароль.
    """

    username_or_email = serializers.CharField(max_length=225)
    password = serializers.CharField(max_length=225)


class RegisterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для регистрации.

    Позволяет пользователям зарегистрироваться, предоставив имя пользователя,
    электронную почту, пароль и подтверждение пароля.
    """

    password = serializers.CharField(write_only=True, min_length=8)
    password_confirmation = serializers.CharField(write_only=True, min_length=8)

    def validate(self, data):
        """
        Проверка данных перед сохранением.

        Проверяет, что пароль и подтверждение пароля совпадают.

        :param data: Входные данные
        :return: Валидированные данные
        """
        password = data.get('password')
        password_confirmation = data.get('password_confirmation')

        if password and password != password_confirmation:
            raise serializers.ValidationError("Пароли не совпадают")

        return data

    def save(self, **kwargs):
        """
        Сохранение пользователя.

        Хеширует пароль перед сохранением.

        :param kwargs: Дополнительные аргументы для сохранения
        :return: Сохраненный объект пользователя
        """
        password = self.validated_data.get('password')
        self.validated_data.pop('password_confirmation')
        self.validated_data['password'] = make_password(password)
        return super().save(**kwargs)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password',
            'password_confirmation',
        )


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'id',
            'avatar',
            'about',
            'address',
            'created_at',
            'updated_at',
        )
