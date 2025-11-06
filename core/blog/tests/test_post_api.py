import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="sedighifardin1@gmail.com", password="12345678*", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:
    client = APIClient()

    def test_get_post_response_200_status(self):
        url = reverse("blog:api-v1:post-list")
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_post_response_403_status(self):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        self.client.force_authenticate(user={})
        response = self.client.post(url, data)
        assert response.status_code == 403

    def test_create_post_response_201_status(self, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
            "status": True,
            "published_date": datetime.now(),
        }
        user = common_user
        self.client.force_login(user=user)
        # self.client.force_authenticate(user=user)
        response = self.client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(self, common_user):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "test",
            "content": "description",
        }
        user = common_user
        self.client.force_login(user=user)
        # self.client.force_authenticate(user=user)
        response = self.client.post(url, data)
        assert response.status_code == 400
