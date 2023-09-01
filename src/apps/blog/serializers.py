from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import (
    Tag,
    Category,
    Post,
    Comment,
)

User = get_user_model()


class TagListSerializer(serializers.ModelSerializer):
    """ Сериализатор списка для модели Тег. """

    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
            'slug',
            'created_at',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор деталей для модели Тег. """

    class Meta:
        model = Tag
        lookup_field = 'slug'
        fields = (
            'id',
            'title',
            'slug',
            'created_at',
            'updated_at',
        )


class CategoryListSerializer(serializers.ModelSerializer):
    """ Сериализатор списка для модели Категория. """

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug',
            'created_at',
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор деталей для модели Категория. """

    class Meta:
        model = Category
        lookup_field = 'slug'
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'created_at',
            'updated_at',
        )


class PostListSerializer(serializers.ModelSerializer):
    """ Сериализатор списка для модели Пост. """

    category = CategoryListSerializer()

    class Meta:
        model = Post
        fields = (
            'id',
            'image',
            'title',
            'slug',
            'category',
            'comments_count',
            'created_at',
        )


class PostDetailSerializer(serializers.ModelSerializer):
    """ Сериализатор деталей для модели Пост. """

    category = CategoryListSerializer()
    tags = TagListSerializer(many=True)

    class Meta:
        model = Post
        fields = (
            'id',
            'image',
            'title',
            'slug',
            'category',
            'tags',
            'comments_count',
            'created_at',
            'updated_at',
        )


class AuthorListSerializer(serializers.ModelSerializer):
    """ Сериализатор список для модели Автор """

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
        )


class CommentListSerializer(serializers.ModelSerializer):
    """ Сериализатор списка для модели Комментарий. """

    author = AuthorListSerializer()

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'author',
            'created_at',
            'updated_at',
        )
