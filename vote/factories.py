from django.contrib.auth.models import User

import factory
import factory.fuzzy

from base.factories import BaseModelFactory
from .models import Image, ImageVote, Recommendation


CHOICES = [-1,1]


class UserFactory(BaseModelFactory):
    class Meta:
        model = User
    
    username = factory.Sequence(lambda n: 'user{}'.format(n))
    password = factory.fuzzy.FuzzyText(length=10)


class ImageFactory(BaseModelFactory):
    class Meta:
        model = Image

    image_name = factory.fuzzy.FuzzyText(length=100)
    url = factory.fuzzy.FuzzyText(length=150)
    creator = factory.SubFactory(UserFactory)


class ImageVoteFactory(BaseModelFactory):
    class Meta:
        model = ImageVote

    image = factory.SubFactory(ImageFactory)
    user = factory.SubFactory(UserFactory)
    vote = factory.fuzzy.FuzzyChoice(CHOICES)


class RecommendationFactory(BaseModelFactory):
    class Meta: 
        model = Recommendation

    subject = factory.fuzzy.FuzzyText(length=100)
    body = factory.fuzzy.FuzzyText(length=250)
    email = factory.fuzzy.FuzzyText(length=250)
    creator = factory.SubFactory(UserFactory)

