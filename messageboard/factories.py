from django.contrib.auth.models import User

import factory
import factory.fuzzy

from base.factories import BaseModelFactory
from vote.factories import UserFactory

from .models import Forum, Topic, TopicVote, TopicComment

UPVOTE = 1
DOWNVOTE = -1
VOTE_CHOICES = (
    (UPVOTE, '+1'),
    (DOWNVOTE, '-1')
)


class ForumFactory(BaseModelFactory):
    class Meta:
        model = Forum

    slug = # need factory equivalent of slug
    moderators = factory.SubFactory(UserFactory)


class TopicFactory(BaseModelFactory):
    class Meta: 
        model = Topic

    forum = factory.SubFactory(ForumFactory)
    user = factory.SubFactory(UserFactory)
    title = factory.fuzzy.FuzzyText(length=100)
    slug = # need to figure out how to handle
    body = factory.fuzzy.FuzzyText(length=300) # Check if this is the same


class TopicCommentFactory(BaseModelFactory):
    class Meta:
        model = TopicComment
    
    topic = factory.SubFactory(TopicFactory)
    parent = # check against reddit
    user = factory.SubFactory(UserFactory)
        body = factory.fuzzy.FuzzyText(length=500) # Check if this is the same


class TopicVoteFactory(BaseModelFactory):
    class Meta:
        model = TopicVote

    user = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)
    vote = factory.fuzzy.FuzzyChoice(VOTE_CHOICES)
