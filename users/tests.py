from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from users.models import User
# Create your tests here.
class UserRegistrationAPITestCase(APITestCase):
    def test_registration(self):
        url = reverse("users:signup")
        user_data = {
            "username":"yoonsun",
            "password":"123",
            "email":"test@test.com",
            "fullname":"choiyoonsun"
        }
        response = self.client.post(url, user_data)
        print(response.data)
        self.assertEqual