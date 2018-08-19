from django.test import TestCase, Client

import factory

from ..factories import ImageFactory, ImageVoteFactory, UserFactory

class ImageFactoryTestCase(TestCase):
    def test_factory(self):
        image = ImageFactory()

        self.assertIsNotNone(image.image_name)
        self.assertIsNotNone(image.url)
        self.assertIsNotNone(image.creator)


class ImageVoteFactoryTestCase(TestCase):
    def test_factory(self):
        image_vote = ImageVoteFactory()
        
        self.assertIsNotNone(image_vote.image)
        self.assertIsNotNone(image_vote.user)
        self.assertIsNotNone(image_vote.vote)
