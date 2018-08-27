from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

import factory

from ..factories import ImageFactory, ImageVoteFactory, UserFactory


class HomeViewTest(TestCase):
    def test_200(self):
        url = reverse("home")
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 200)


class ImageDetailViewTestCase(TestCase):
    def test_200(self):
        url = reverse("contact_us")
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
