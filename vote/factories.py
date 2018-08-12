from django.contrib.auth.models import User

import factory 
import factory.fuzzy

from base.factories import BaseModelFactory

from .models import Image, Comment, ImageVote, CommentVote

class UserFactory(factory.Django.DjangoModelFactory):
    class Meta:
        model = User
    
    username = factory.Sequence(lambda n: 'user{}'.format(n))
    password = factory.fuzzy.FuzzyText(length=10)


class ImageFactory(factory.Django.DjangoModelFactory):
    class Meta:
        model = Image

    image_name = fuzzy.FuzzyText(length=100)
    url = fuzzy.FuzzyText(length=150)
    creator = factory.SubFactory(UserFactory)


class ImageVoteFactory(factory.Django.DjangoModelFactory):
    class Meta:
        model = ImageVote
    
    image = factory.SubFactory(ImageFactory)
    user = factory.SubFactory(UserFactory)
    vote = fuzzy.FuzzyChoice("-1", "1")


class CommentFactory(factory.Django.DjangoModelFactory):
    class Meta:
        model = Comment

    image = factory.SubFactory(ImageFactory)
    user = factory.SubFactory(UserFactory)
    body = fuzzy.FuzzyText(length=250)


class CommentVoteFactory(factory.Django.DjangoModelFactory):
    class Meta:
        model = CommentVote
    
    comment = factory.SubFactory(CommentFactory)
    user = factory.SubFactory(UserFactory)
    vote = fuzzy.FuzzyChoice("-1", "1")
