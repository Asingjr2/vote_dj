from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy


class MapHomeViewTestCase(TestCase):
    def test_200(self):
        """
        URL requires 'route' object to parse origin and destination information for directions.
        """

        data = {"route":"place"}
        url = reverse("locations:home")
        client = Client()
        response = client.get(url, data)

        self.assertEqual(response.status_code, 200)

    def test_successful_post(self):
        """Successful post should return redirect."""

        data = {"origin":"place", "destination":"another place"}
        url = reverse("locations:home")
        client = Client()
        response = client.post(url, data)

        self.assertEqual(response.status_code, 302)

    def test_successful_post_follow(self):
        """Successful post should follow to successful get request."""

        data = {"origin":"place", "destination":"another place"}
        url = reverse("locations:home")
        client = Client()
        response = client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_unsuccessful_post(self):
        """
        Posting direction request without orign should redirect.
        """
        url = reverse("locations:home")
        client = Client()
        response = client.post(url)

        self.assertEqual(response.status_code, 302)


class ParkViewTestCase(TestCase):
    def test_200(self):
        url = reverse("locations:parks")
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 200)
