from django.contrib.auth.models import User

import factory
import factory.fuzzy

from base.factories import BaseModelFactory

from .models import Image,ImageVote


CHOICES = [-1,1]
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
    
    username = factory.Sequence(lambda n: 'user{}'.format(n))
    password = factory.fuzzy.FuzzyText(length=10)


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image

    image_name = factory.fuzzy.FuzzyText(length=100)
    url = factory.fuzzy.FuzzyText(length=150)
    creator = factory.SubFactory(UserFactory)


class ImageVoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ImageVote

    image = factory.SubFactory(ImageFactory)
    user = factory.SubFactory(UserFactory)
    vote = factory.fuzzy.FuzzyChoice(CHOICES)
