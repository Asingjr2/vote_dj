from django.test import TestCase, Client

import factory

from ..factories import VolunteerApplicationFactory, VolunteerJobFactoy


class VolunteerJobFactoyTestCase(TestCase):
    def test_factory(self):
        volunteer_job = VolunteerJobFactoy()

    self.assertIsNone(application.location)
    self.assertIsNone(application.title)


class VolunteerApplicationFactoryTestCase(TestCase):
    def test_factory(self):
        application = VolunteerApplicationFactory()

    self.assertIsNone(application.job)
    self.assertIsNone(application.first_name)
    self.assertIsNone(application.last_name)
    self.assertIsNone(application.about_you)

    # Compare with factory
    self.assertIsNone(application.email)
    self.assertIsNone(application.contact_number)
