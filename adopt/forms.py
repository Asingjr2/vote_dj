from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm

from .models import Animal, Application


class ApplicationForm(ModelForm):
    """
    Creating that will be modified in template with crispy form.  Validation handled in models.
    """

    class Meta:
        model = Application
        exclude = ("pets", "applicant")
