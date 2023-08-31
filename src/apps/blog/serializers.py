from rest_framework import serializers
from .models import (
    Tag,
    Category,
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
