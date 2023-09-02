from django.urls import path
from .views import (
    TagListAPIView,
    TagDetailAPIView,
    GetPostsByTagAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    GetPostsByCategoryAPIView,
    PostListCreateAPIView,
    GetCommentsByPostAPIView,
    PostRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    # tags
    path('tags/', TagListAPIView.as_view()),
    path('tags/<slug:slug>/', TagDetailAPIView.as_view()),
    path('tags/<slug:slug>/posts/', GetPostsByTagAPIView.as_view()),

    # categories
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<slug:slug>/', CategoryDetailAPIView.as_view()),
    path('categories/<slug:slug>/posts/', GetPostsByCategoryAPIView.as_view()),

    # posts
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<slug:slug>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('posts/<slug:slug>/comments/', GetCommentsByPostAPIView.as_view()),
]
