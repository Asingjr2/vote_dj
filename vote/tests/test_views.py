from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

import factory

from ..factories import ImageFactory, ImageVoteFactory, UserFactory


class HomeViewTest(TestCase):
    pass

class ImageDetailViewTestCase(TestCase):
    pass


class ImageDeleteViewTestCase(TestCase):
    pass


class ImageUpvoteViewTestCase(TestCase):
    pass


class ImageDownvoteViewTestCase(TestCase):
    pass
