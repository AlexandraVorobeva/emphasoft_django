from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserTestCase(APITestCase):
    profile_list_url = reverse("all-users")

    def setUp(self):
        self.user = self.client.post(
            "/auth/users/",
            data={"username": "Alexandra1", "password": "1234HelloWorld"},
        )
        response = self.client.post(
            "/auth/jwt/create/",
            data={"username": "Alexandra1", "password": "1234HelloWorld"},
        )
        self.token = response.data["access"]
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_UserList(self):
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_UserList_negative(self):
        self.client.force_authenticate(user=None)
        response = self.client.get(self.profile_list_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_UserDetail(self):
        response = self.client.get(reverse("user", kwargs={"pk": 1}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
