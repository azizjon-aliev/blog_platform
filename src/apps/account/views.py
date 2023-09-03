from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import (
    LoginSerializer,
    RegisterSerializer,
    ProfileSerializer
)
from src.apps.blog.models import Post
from src.apps.blog.views import PostListAPIView
from src.utils.functions import is_valid_email

User = get_user_model()


class RegisterAPIView(generics.CreateAPIView):
    """
    API-представление для регистрации пользователя.

    Позволяет пользователям зарегистрироваться, предоставив свои учетные данные.
    """

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    authentication_classes = ()

    @extend_schema(
        responses={
            201: {"type": "object", "properties": {
                "type": {"type": "string", "description": "Тип токена (Bearer)"},
                "refresh": {"type": "string", "description": "Refresh токен"},
                "access": {"type": "string", "description": "Access токен"},
            }},
        },
    )
    def post(self, request):
        """
        Обработка регистрации пользователя.

        В случае успешной регистрации возвращает JWT-токен доступа.

        :param request: HTTP-запрос
        :return: Ответ с JWT-токенами
        """
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Создаем RefreshToken для нового пользователя
            refresh = RefreshToken.for_user(serializer.save())

            return Response(
                data={
                    "type": "Bearer",
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.CreateAPIView):
    """
    API-представление для входа пользователя.

    Позволяет пользователям войти, предоставив свои учетные данные (имя пользователя или электронную почту и пароль).
    """

    queryset = User.objects.all()
    serializer_class = LoginSerializer
    authentication_classes = ()

    @extend_schema(
        responses={
            201: {"type": "object", "properties": {
                "type": {"type": "string", "description": "Тип токена (Bearer)"},
                "refresh": {"type": "string", "description": "Refresh токен"},
                "access": {"type": "string", "description": "Access токен"},
            }},
        },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        """
        Обработка входа пользователя.

        В случае успешного входа возвращает JWT-токен доступа.

        :param request: HTTP-запрос
        :return: Ответ с JWT-токенами
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username_or_email = serializer.data.get('username_or_email')
        password = serializer.data.get('password')

        # Проверяем, предоставленный идентификатор - это электронная почта или имя пользователя
        if is_valid_email(username_or_email):
            user = User.objects.filter(email=username_or_email).first()
        else:
            user = User.objects.filter(username=username_or_email).first()

        if user and user.check_password(password):
            # Создаем RefreshToken для аутентифицированного пользователя
            refresh = RefreshToken.for_user(user)

            return Response(
                data={
                    "type": "Bearer",
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            data={"detail": "Неверные учетные данные"},
            status=status.HTTP_400_BAD_REQUEST
        )


class ProfilePostListAPIView(PostListAPIView):
    """
    API-представление для получения списка собственных постов пользователя.

    Это представление позволяет аутентифицированным пользователям получить список своих собственных постов.
    """

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Получить запрос для выборки постов аутентифицированного пользователя.

        :return: Запрос для выборки постов
        """
        return Post.objects.filter(author=self.request.user)


class ProfileAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ API view for model profile
    """

    queryset = Post.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        instance = request.user.profile
        return Response(self.get_serializer(instance).data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        instance = request.user.profile
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(self.get_serializer(instance).data)

    def patch(self, request, *args, **kwargs):
        instance = request.user.profile
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(self.get_serializer(instance).data)

    def delete(self, request, *args, **kwargs):
        instance = request.user
        instance.is_active = False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


