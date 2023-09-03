from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from .models import Tag, Category, Post

User = get_user_model()


class BlogAPITestCase(APITestCase):
    def setUp(self):
        self.url = '/api/v1'

        # Создаем пользователя для тестов
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_tag_list(self):
        # Проверяем, что запрос списка тегов возвращает статус 200
        url = f"{self.url}/tags/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tag_detail(self):
        # Создаем тег и проверяем, что запрос деталей тега возвращает статус 200 и правильное название
        tag = Tag.objects.create(
            title='Test Tag',
            slug="test-tag",
            author=self.user,
        )
        url = f"{self.url}/tags/{tag.slug}/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Tag')

    def test_tags_associated_with_posts(self):
        # Создаем тег, категорию и пост, связанные с тегом, и проверяем, что запрос списка постов по тегу возвращает
        # статус 200 и правильные данные
        tag = Tag.objects.create(
            title='Test Tag',
            slug="test-tag",
            author=self.user,
        )
        category = Category.objects.create(
            title='Test Category',
            slug="test-category",
            author=self.user,
        )

        url = f"{self.url}/tags/{tag.slug}/posts/"

        post = Post.objects.create(
            title='Test Post',
            slug="test-post",
            description='This is a test post description.',
            category=category,
            author=self.user,
        )
        post.tags.add(tag)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
        self.assertEqual(response.data['results'][0]['title'], 'Test Post')

    def test_category_list(self):
        # Проверяем, что запрос списка категорий возвращает статус 200
        url = f"{self.url}/categories/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_categories_detail(self):
        # Создаем категорию и проверяем, что запрос деталей категории возвращает статус 200 и правильное название
        category = Category.objects.create(
            title='Test Category',
            slug="test-category",
            author=self.user,
        )
        url = f"{self.url}/categories/{category.slug}/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Category')

    def test_posts_associated_with_posts(self):
        # Создаем категорию, тег и пост, связанные с категорией и тегом, и проверяем, что запрос списка постов по
        # категории возвращает статус 200 и правильные данные
        category = Category.objects.create(
            title='Test Category',
            slug="test-category",
            author=self.user,
        )
        tag = Tag.objects.create(
            title='Test Tag',
            slug="test-tag",
            author=self.user,
        )

        url = f"{self.url}/categories/{tag.slug}/posts/"

        post = Post.objects.create(
            title='Test Post',
            slug="test-post",
            description='This is a test post description.',
            category=category,
            author=self.user,
        )
        post.tags.add(tag)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
