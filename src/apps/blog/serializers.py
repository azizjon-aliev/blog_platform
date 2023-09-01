from rest_framework import serializers
from .models import (
    Tag,
    Category,
    Post,
    Comment,
)


class TagListSerializer(serializers.ModelSerializer):
    """ List serializer for tag model """

    class Meta:
        model = Tag
        fields = (
            'id',
            'title',
            'slug',
            'created_at',
        )


class TagDetailSerializer(serializers.ModelSerializer):
    """ Detail serializer for tag model """

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
    """ List serializer for category model """

    class Meta:
        model = Category
        fields = (
            'id',
            'title',
            'slug',
            'created_at',
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    """ Detail serializer for category model """

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
    """ List serializer for post model """
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
    """ Detail serializer for post model """
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


class CommentListSerializer(serializers.ModelSerializer):
    """ List serializer for comment model """

    class Meta:
        model = Comment
        fields = (
            'id',
            'text',
            'created_at',
            'updated_at',
        )
