import factory
import factory.fuzzy

from .models import Animal, Application
from base.factories import BaseModelFactory

AGE_RANGES = (
    ("6 months", "6 months"), 
    ("1 YEAR", "1 YEAR"), 
    ("2-5 YEARS", "2-5 YEARS"), 
    ("5-10 YEARS", "5-10 YEARS"), 
    ("10 YEARS OR OLDER", "10 YEARS OR OLDER"))

GENDER = (
    ("male", "MALE"), 
    ("female", "FEMALE")
)

ANIMAL_TYPE = (
    ("dog", "DOG"), 
    ("cat", "CAT"),
    ("other", "OTHER")
)


class AnimalFactory(BaseModelFactory):
    class Meta:
        model = Animal

    name = factory.fuzzy.FuzzyText(length=100)
    age = factory.fuzzy.FuzzyChoice(AGE_RANGES)
    gender = factory.fuzzy.FuzzyChoice(GENDER)
    animal_type = factory.fuzzy.FuzzyChoice(ANIMAL_TYPE)
    breed = factory.fuzzy.FuzzyText(length=100)
    picture = factory.fuzzy.FuzzyText(length=100)
    description = factory.fuzzy.FuzzyText(length=250)


class ApplicationFactory(BaseModelFactory):
    class Meta:
        model = Application

    # pet = factory.SubFactory(AnimalFactory)
    first_name = factory.fuzzy.FuzzyText(length=50)
    last_name = factory.fuzzy.FuzzyText(length=50)
    street_address = factory.fuzzy.FuzzyText(length=250)
    street_address_2 = factory.fuzzy.FuzzyText(length=250)
    state = factory.fuzzy.FuzzyText(length=2)
    family_size = factory.fuzzy.FuzzyInteger(1, 10)
    pets_dogs = factory.fuzzy.FuzzyInteger(0,5)
    pets_cats = factory.fuzzy.FuzzyInteger(0,4)
    pets_other = factory.fuzzy.FuzzyInteger(0,5)
    contact_number = factory.fuzzy.FuzzyInteger(1000000000, 9999999999)



