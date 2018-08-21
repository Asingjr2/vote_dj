from django.test import TestCase, Client

import factory

from ..factories import ForumFactory, TopicFactory, TopicVoteFactory, TopicCommentFactory


class ForumFactoryTestCase(TestCase):
    def test_factory(self):
        forum = ForumFactory()

    self.assertIsNotNone(forum.slug)
    self.assertIsNotNone(forum.moderators)
    self.assertIsNotNone(forum.created_at)
    self.assertIsNotNone(forum.updated_at)


class TopicFactoryTestCase(TestCase):
    def test_factory(self):
        topic = TopicFactory()

    self.assertIsNotNone(topic.forum)
    self.assertIsNotNone(topic.user)
    self.assertIsNotNone(topic.title)
    self.assertIsNotNone(topic.slug)
    self.assertIsNotNone(topic.body)


class TopicVoteFactoryTestCase(TestCase):
    def test_factory(self):
        topic_vote = TopicVoteFactory()
    
    self.assertIsNotNone(topic_vote.user)
    self.assertIsNotNone(topic_vote.topic)
    self.assertIsNotNone(topic_vote.vote)


class TopicCommentFactoryTestCase(TestCase):
    def test_factory(self):
        comment = TopicCommentFactory()
    
    self.assertIsNotNone(comment.topic)
    self.assertIsNotNone(comment.parent)### Check against reddit
    self.assertIsNotNone(comment.user)
    self.assertIsNotNone(comment.body)
