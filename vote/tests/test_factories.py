from django.test import TestCase, Client

import factory

from ..factories import ImageFactory, ImageVoteFactory, CommentFactory, CommentVoteFactory, UserFactory

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


class CommentFactoryTestCase(TestCase):
    def test_factory(self):
        comment = CommentFactory()
        
        self.assertIsNotNone(comment.image)
        self.assertIsNotNone(comment.user)
        self.assertIsNotNone(comment.body)


class CommentVoteFactoryTestCase(TestCase):
    def test_factory(self):
        comment_vote = CommentVoteFactory()
        
        self.assertIsNotNone(comment_vote.comment)
        self.assertIsNotNone(comment_vote.user)
        self.assertIsNotNone(comment_vote.vote)
