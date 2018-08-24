from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator, MinLengthValidator, EmailValidator, MaxValueValidator, MinValueValidator
from django.urls import reverse

from base.models import BaseModel

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


class Animal(BaseModel):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=20, choices=AGE_RANGES)
    gender = models.CharField(max_length=10, choices=GENDER, default="male")
    animal_type = models.CharField(max_length=10, choices=ANIMAL_TYPE, default="dog")
    breed = models.CharField(max_length=100, blank=True, null=True)
    picture = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(validators=[MaxLengthValidator(250), MinLengthValidator(10)])

    def __str__(self):
        return "Name {}, Type {}".format(self.name, self.animal_type)


class Application(BaseModel):
    pet = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="pet application"),
    # applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    street_address = models.CharField(max_length=250)
    street_address_2 = models.CharField(max_length=250, blank=True, null=True)
    state = models.CharField(max_length=2)
    family_size = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    # current_pets_total = models.IntegerField()
    pets_dogs = models.IntegerField(validators=[MaxValueValidator(5, "This breed requires attention than you can provide at this time."), MinValueValidator(0)])
    pets_cats = models.IntegerField(validators=[MaxValueValidator(4), MinValueValidator(0)], blank=True, null=True)
    pets_other = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(0)], blank=True, null=True)
    interest_reason = models.TextField(validators=[MaxLengthValidator(250), MinLengthValidator(10)])
    email = models.EmailField(validators = [EmailValidator()])
    contact_number = models.IntegerField(validators=[MinValueValidator(1000000000), MaxLengthValidator(9999999999)], blank=True, null=True)

    def __str__(self):
        return "{} applying for {}".format(self.first_name, self.pet)

