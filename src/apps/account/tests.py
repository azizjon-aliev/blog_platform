from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountAPITestCase(APITestCase):
    def setUp(self):
        self.url = '/api/v1/account'

        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_register_user(self):
        """
        Тестирование регистрации нового пользователя.
        """
        url = f"{self.url}/register/"

        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword',
            'password_confirmation': 'newpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_login_user(self):
        """
        Тестирование входа пользователя.
        """
        url = f"{self.url}/login/"

        data = {
            'username_or_email': 'testuser',
            'password': 'testpassword',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)

    def test_get_user_profile(self):
        """
        Тестирование получения профиля пользователя.
        """
        self.client.force_authenticate(user=self.user)

        url = f"{self.url}/profile/"

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_change_user_profile(self):
        """
        Тестирование изменения профиля пользователя.
        """
        self.client.force_authenticate(user=self.user)

        url = f"{self.url}/profile/"

        data = {
            'about': 'Updated about information',
            'address': 'Updated address',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['about'], 'Updated about information')
        self.assertEqual(response.data['address'], 'Updated address')

    def test_delete_user_profile(self):
        """
        Тестирование удаления профиля пользователя.
        """
        self.client.force_authenticate(user=self.user)

        url = f"{self.url}/profile/"

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.user.refresh_from_db()
        self.assertFalse(self.user.is_active)
