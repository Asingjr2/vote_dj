from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import VolunteerApplication


class VolunteerApplicationForm(ModelForm):
    """
    Creating form for jobs at different site locations.  Will allow sorting on page.
    """
    class Meta:
        model = VolunteerApplication
        fields = ["first_name", "last_name","about_you", "email", "contact_number" ]
        exclude = ("job",)
