from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterAPIView,
    LoginAPIView,
    ProfilePostListAPIView,
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),

    path('token/refresh/', TokenRefreshView.as_view()),

    # profile
    path('profile/posts/', ProfilePostListAPIView.as_view()),
]
