from django.test import TestCase

import factory

from ..factories import AnimalFactory, ApplicationFactory


class AnimalFactoryTestCase(TestCase):
    def test_factory(self):
        animal = AnimalFactory()

        self.assertIsNotNone(animal.name)
        self.assertIsNotNone(animal.age)
        self.assertIsNotNone(animal.gender)
        self.assertIsNotNone(animal.animal_type)
        self.assertIsNotNone(animal.breed)
        self.assertIsNotNone(animal.picture)
        self.assertIsNotNone(animal.description)


class ApplicationFactoryTestCase(TestCase):
    def test_factory(self):
        application = ApplicationFactory()

        # self.assertIsNotNone(application.pet)
        self.assertIsNotNone(application.first_name)
        self.assertIsNotNone(application.last_name)
        self.assertIsNotNone(application.street_address)
        self.assertIsNotNone(application.street_address_2)
        self.assertIsNotNone(application.state)
        self.assertIsNotNone(application.family_size)
        self.assertIsNotNone(application.pets_dogs)
        self.assertIsNotNone(application.pets_cats)
        self.assertIsNotNone(application.pets_other)
        self.assertIsNotNone(application.contact_number)
