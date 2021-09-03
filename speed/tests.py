from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import CustomUser
from rest_framework.authtoken.models import Token

class RegistrationTestCase(APITestCase):
    def test_registration(self):
        data = {
            "username": "testcase",
            "email": "test@gmail.com",
            "password1": "qwerty_111",
            "password2": "qwerty_111",
        }
        response = self.client.post("/api/rest-auth/registration/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class UserDataViewSetTestCase(APITestCase):


    def setUp(self):
        self.user = CustomUser.objects.create_user(username="davinci", password="qwerty_123")
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_profile_list_authenticated(self):
        response = self.client.get('http://127.0.0.1:8000/api/speed/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_profile_list_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.get('http://127.0.0.1:8000/api/speed/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)