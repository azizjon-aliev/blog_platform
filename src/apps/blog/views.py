from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import (
    Tag,
    Category,
)
from .serializers import (
    TagListSerializer,
    TagDetailSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
)


class TagListAPIView(generics.ListAPIView):
    """ List api view for tag model """

    queryset = Tag.objects.all()
    serializer_class = TagListSerializer
    authentication_classes = ()
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = (
        'title',
        'slug',
    )
    ordering_fields = (
        'title',
    )


class TagDetailAPIView(generics.RetrieveAPIView):
    """ Detail api view for tag model """

    queryset = Tag.objects.all()
    serializer_class = TagDetailSerializer
    authentication_classes = ()
    lookup_field = 'slug'


class CategoryListAPIView(generics.ListAPIView):
    """ List api view for category model """

    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
    authentication_classes = ()
    filter_backends = (
        SearchFilter,
        OrderingFilter,
    )
    search_fields = (
        'title',
        'slug',
        'description',
    )
    ordering_fields = (
        'title',
    )


class CategoryDetailAPIView(generics.RetrieveAPIView):
    """ Detail api view for category model """

    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    authentication_classes = ()
    lookup_field = 'slug'
