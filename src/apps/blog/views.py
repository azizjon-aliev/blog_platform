from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import (
    Tag,
    Category,
    Post,
    Comment,
)
from .serializers import (
    TagListSerializer,
    TagDetailSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    PostListSerializer,
    PostDetailSerializer,
    CommentListSerializer,
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


class GetPostsByTagAPIView(generics.ListAPIView):
    """ Get posts by tag api view """

    serializer_class = PostListSerializer
    authentication_classes = ()

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(tags__slug=slug)


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


class GetPostsByCategoryAPIView(generics.ListAPIView):
    """ Get posts by category api view """

    authentication_classes = ()

    def get_serializer_class(self):
        class ChangePostListSerializer(PostListSerializer):
            class Meta:
                model = PostListSerializer.Meta.model
                fields = list(PostListSerializer.Meta.fields).copy()
                fields.remove('category')

        return ChangePostListSerializer

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Post.objects.filter(category__slug=slug)


class PostListAPIView(generics.ListAPIView):
    """ List api view for post model """

    queryset = Post.objects.all()
    serializer_class = PostListSerializer
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


class PostDetailAPIView(generics.RetrieveAPIView):
    """ Detail api view for post model """

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
    authentication_classes = ()
    lookup_field = 'slug'


class GetCommentsByPostAPIView(generics.ListAPIView):
    """ Get comments by post api view """

    serializer_class = CommentListSerializer
    authentication_classes = ()

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Comment.objects.filter(post__slug=slug)