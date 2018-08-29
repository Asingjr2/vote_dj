from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

from ..factories import VolunteerApplicationFactory, VolunteerJobFactory


class JobListingViewTestCase(TestCase):
    def test_200(self):
        
        url = reverse("volunteer:jobs_listing")
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class VolunteerApplicationFormViewTestCase(TestCase):
    def test_200(self):
        job = VolunteerJobFactory()
        
        url = "/volunteer/apply/{}".format(job.id)
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_200_post(self):
        job = VolunteerJobFactory()
        
        url = "/volunteer/apply/{}".format(job.id)
        client = Client()
        data = {}
        response = client.post(url, data, follow=True)
        self.assertEqual(response.status_code, 200)
