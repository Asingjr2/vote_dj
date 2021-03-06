from django.test import TestCase, Client

import factory

from ..factories import ImageFactory, ImageVoteFactory, UserFactory, RecommendationFactory


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


class RecommendationFactoryTestCase(TestCase):
    def test_factory(self):
        recommendation = RecommendationFactory()

        self.assertIsNotNone(recommendation.subject)
        self.assertIsNotNone(recommendation.body)
        self.assertIsNotNone(recommendation.email)
        self.assertIsNotNone(recommendation.creator)

