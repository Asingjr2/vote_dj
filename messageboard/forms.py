from django import forms
from django.forms import ModelForm, HiddenInput

from .models import Forum, Topic, TopicComment


class ForumUpdateForm(ModelForm):
    class Meta:
        model = Forum
        fields = ('slug',)
     

class ForumCreateForm(ModelForm):
    class Meta:
        model = Forum
        fields = ("slug",)
        labels = {
            "slug": "Forum Title"
        }


class TopicCreateForm(ModelForm):
    class Meta:
        model = Topic
        fields = ("title","body",)
        widgets = {
        "body": forms.Textarea(attrs = {
            "label": "",
            "placeholder": "Add new message", 
            "maxLength":"300", 
        }), 
        }


class TopicCommentCreateForm(ModelForm):
    class Meta:
        model = TopicComment
        fields = ("body",)
        widgets = {
        "body": forms.Textarea(attrs = {
            "class": "form-control",
            "label": "",
            "placeholder": "Add new comment", 
            "maxLength":"250", 
        }), 
        }
