from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import (
    MaxLengthValidator,
    MinLengthValidator,
    EmailValidator,
    MaxValueValidator,
    MinValueValidator
)

from base.models import BaseModel


LOCATIONS = (
    ("Alexandria", "Alexandria Location"),
    ("Springfield", "Springfield Location"),
    ("Arlington", "Arlington Location"),
    ("Woodbridge", "Woodbridge Location"),
    ("Falls Church", "Falls Church Location"),
)

HOURS = (
    ("part-time", "part-time"),
    ("full-time", "full-time")
)


class VolunteerJob(BaseModel):
    location = models.CharField(max_length=20, choices=LOCATIONS)
    title = models.CharField(max_length=50)
    hours = models.CharField(max_length=20, choices=HOURS)


class VolunteerApplication(BaseModel):
    job = models.ForeignKey(VolunteerJob, on_delete=models.CASCADE, related_name="job application"),
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    about_you = models.TextField(validators=[MaxLengthValidator(250), MinLengthValidator(10)])
    email = models.EmailField(validators = [EmailValidator()])
    contact_number = models.IntegerField(validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)], blank=True, null=True)

    