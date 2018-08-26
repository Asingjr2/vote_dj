from django.contrib.auth.models import User

import factory
import factory.fuzzy

from base.factories import BaseModelFactory
from vote.factories import UserFactory

from .models import Forum, Topic, TopicVote, TopicComment

UPVOTE = 1
DOWNVOTE = -1
VOTE_CHOICES = [-1,1]


class ForumFactory(BaseModelFactory):
    class Meta:
        model = Forum

    slug = factory.Sequence(lambda n: 'forum-{}'.format(n))


class TopicFactory(BaseModelFactory):
    class Meta: 
        model = Topic

    forum = factory.SubFactory(ForumFactory)
    user = factory.SubFactory(UserFactory)
    title = factory.fuzzy.FuzzyText(length=100)
    body = factory.fuzzy.FuzzyText(length=300) 


class TopicCommentFactory(BaseModelFactory):
    class Meta:
        model = TopicComment
    
    topic = factory.SubFactory(TopicFactory)
    user = factory.SubFactory(UserFactory)
    body = factory.fuzzy.FuzzyText(length=500) 


class TopicVoteFactory(BaseModelFactory):
    class Meta:
        model = TopicVote

    user = factory.SubFactory(UserFactory)
    topic = factory.SubFactory(TopicFactory)
    vote = factory.fuzzy.FuzzyChoice(VOTE_CHOICES)
