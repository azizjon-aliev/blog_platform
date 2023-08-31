from django.urls import path
from .views import (
    TagListAPIView,
    TagDetailAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
)

urlpatterns = [
    path('tags/', TagListAPIView.as_view()),
    path('tags/<slug:slug>/', TagDetailAPIView.as_view()),
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<slug:slug>/', CategoryDetailAPIView.as_view()),
]
