from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

from ..factories import AnimalFactory, ApplicationFactory


class AnimalListingTestCase(TestCase):
    def test_200(self):

        url = reverse("adopt:adopt_all")
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 200)


class DogListingTestCase(TestCase):
    def test_200(self):

        url = reverse("adopt:adopt_dogs")
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 200)


class CatListingTestCase(TestCase):
    def test_200(self):

        url = reverse("adopt:adopt_cats")
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 200)


class OtherAnimalListingTestCase(TestCase):
    def test_200(self):

        url = reverse("adopt:adopt_other")
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 200)


class AdoptFormTestCase(TestCase):
    def test_200(self):
        pet = AnimalFactory()
        
        url = "/adopt/adopt_form/{}".format(pet.id)
        client = Client()
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_successful_post(self):
        pet = AnimalFactory()
        
        url = "/adopt/adopt_form/{}".format(pet.id)
        client = Client()
        data = {}
        response = client.post(url, data, follow=True)

        self.assertEqual(response.status_code, 200)

    def test_unsuccessful_post(self):
        """
        Inccorect post returns user to same page rendering the template with existing forms data along with prompts to correct inaccurate fields.
        """
        pet = AnimalFactory()
        
        url = "/adopt/adopt_form/{}".format(pet.id)
        client = Client()
        response = client.post(url, follow=True)

        self.assertEqual(response.status_code, 200)





