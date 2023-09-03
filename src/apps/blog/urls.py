from django.urls import path
from .views import (
    TagListAPIView,
    TagDetailAPIView,
    GetPostsByTagAPIView,
    CategoryListAPIView,
    CategoryDetailAPIView,
    GetPostsByCategoryAPIView,
    PostListCreateAPIView,
    GetCreateCommentsByPostAPIView,
    PostRetrieveUpdateDestroyAPIView,
    CommentDetailAPIView,
)

urlpatterns = [
    # tags
    path('tags/', TagListAPIView.as_view()),
    path('tags/<str:slug>/', TagDetailAPIView.as_view()),
    path('tags/<str:slug>/posts/', GetPostsByTagAPIView.as_view()),

    # categories
    path('categories/', CategoryListAPIView.as_view()),
    path('categories/<str:slug>/', CategoryDetailAPIView.as_view()),
    path('categories/<str:slug>/posts/', GetPostsByCategoryAPIView.as_view()),

    # comments
    path('comments/<int:pk>/', CommentDetailAPIView.as_view()),

    # posts
    path('posts/', PostListCreateAPIView.as_view()),
    path('posts/<str:slug>/', PostRetrieveUpdateDestroyAPIView.as_view()),
    path('posts/<str:slug>/comments/', GetCreateCommentsByPostAPIView.as_view()),
]
