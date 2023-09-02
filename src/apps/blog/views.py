from rest_framework import generics, status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import (
    Tag,
    Category,
    Post,
    Comment,
)
from .permissions import IsAuthor
from .serializers import (
    TagListSerializer,
    TagDetailSerializer,
    CategoryListSerializer,
    CategoryDetailSerializer,
    PostListSerializer,
    PostDetailSerializer,
    CommentListSerializer,
    PostCreateSerializer,
    PostUpdateSerializer,
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


class PostListCreateAPIView(PostListAPIView, generics.CreateAPIView):
    """ List create api view for post model """

    def get_serializer_class(self):
        if self.request.method == 'GET':
            self.authentication_classes = ()
            return super().get_serializer_class()
        return PostCreateSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return ()
        return (IsAuthenticated(),)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(PostDetailSerializer(instance).data, status=status.HTTP_201_CREATED)


class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """ Detail api view for post model """

    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.request.method == 'GET':
            self.authentication_classes = ()
            return super().get_serializer_class()
        return super().get_serializer_class()

    def get_permissions(self):
        if self.request.method == 'GET':
            return ()
        if self.request.method == 'POST':
            return (
                IsAuthenticated(),
            )
        return (
            IsAuthenticated(),
            IsAuthor(),
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}
        return Response(PostDetailSerializer(instance).data)


class GetCommentsByPostAPIView(generics.ListAPIView):
    """ Get comments by post api view """

    serializer_class = CommentListSerializer
    authentication_classes = ()

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Comment.objects.filter(post__slug=slug)
