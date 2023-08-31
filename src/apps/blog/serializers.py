from rest_framework import serializers
from . import models


class CategoryListSerializer(serializers.ModelSerializer):
    """ List serializer for category model """

    class Meta:
        model = models.Category
        fields = (
            'id',
            'title',
            'slug',
            'created_at',
        )


class CategoryDetailSerializer(serializers.ModelSerializer):
    """ Detail serializer for category model """

    class Meta:
        model = models.Category
        lookup_field = 'slug'
        fields = (
            'id',
            'title',
            'slug',
            'description',
            'created_at',
            'updated_at',
        )
