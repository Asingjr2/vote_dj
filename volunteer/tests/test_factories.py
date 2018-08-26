from django.test import TestCase, Client

import factory

from ..factories import VolunteerApplicationFactory, VolunteerJobFactory


class VolunteerJobFactoyTestCase(TestCase):
    def test_factory(self):
        volunteer_job = VolunteerJobFactory()

        self.assertIsNotNone(volunteer_job.location)
        self.assertIsNotNone(volunteer_job.title)
        self.assertIsNotNone(volunteer_job.hours)


class VolunteerApplicationFactoryTestCase(TestCase):
    def test_factory(self):
        application = VolunteerApplicationFactory()
        new_job = VolunteerJobFactory()

        self.assertIsNotNone(application.job)
        self.assertIsNotNone(application.first_name)
        self.assertIsNotNone(application.last_name)
        self.assertIsNotNone(application.about_you)
        self.assertIsNotNone(application.email)
        self.assertIsNotNone(application.contact_number)
