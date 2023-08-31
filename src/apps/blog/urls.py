from django.urls import path
from .views import (
    CategoryListAPIView,
    CategoryDetailAPIView,
)

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<slug:slug>/', CategoryDetailAPIView.as_view()),
]