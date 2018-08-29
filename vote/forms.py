from django.contrib.auth.models import User 
from django import forms
from django.forms import ModelForm, TextInput, Textarea, EmailInput

from .models import Recommendation


class RecommendationForm(ModelForm):
    """
    Creating form that leaves out creator which can be added automatically if user is logged in.  
    If user not logged in email will be saved.
    """
    
    class Meta:
        model = Recommendation
        fields = ["subject", "body", "email"]
        widgets = {
        "subject": forms.TextInput(attrs = {
            "class": "form-control",
            "label": "Subject",
            "placeholder": "Whats the topic", 
            "maxLength":"110", 
        }), 
        "body": forms.Textarea(attrs = {
            "class": "form-control",
            "label": "message",
            "placeholder": "Add new message", 
            "maxLength":"250", 
        }), 
        "email":forms.EmailInput(attrs= {
            "class": "form-control",
            "label": "Email",
            "placeholder": "Enter valid email" 
        })
    }
