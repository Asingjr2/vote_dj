from django.contrib.auth.models import User

import factory
import factory.fuzzy

from base.factories import BaseModelFactory
from vote.factories import UserFactory
from .models import VolunteerJob, VolunteerApplication


LOCATIONS = (
    ("Alexandria", "Alexandria Location"),
    ("Springfield", "Springfield Location"),
    ("Arlington", "Arlington Location"),
    ("Woodbridge", "Woodbridge Location"),
    ("Falls Church", "Falls Church Location"),
)

HOURS = (
    ("part-time", "part-time"),
    ("full-time", "full-time")
)


class VolunteerJobFactory(BaseModelFactory):
    class Meta:
        model = VolunteerJob

    location = factory.fuzzy.FuzzyChoice(LOCATIONS)
    title = factory.fuzzy.FuzzyText(length=50)
    hours = factory.fuzzy.FuzzyChoice(HOURS)


class VolunteerApplicationFactory(BaseModelFactory):
    class Meta:
        model = VolunteerApplication

    # job = factory.SubFactory(VolunteerJobFactory)
    first_name = factory.fuzzy.FuzzyText(length=50)
    last_name = factory.fuzzy.FuzzyText(length=50)
    about_you = factory.fuzzy.FuzzyText(length=50)
    email = factory.fuzzy.FuzzyText(length=50)
    contact_number = factory.fuzzy.FuzzyInteger(1000000000, 9999999999)
