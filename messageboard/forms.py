from django import forms
from django.forms import ModelForm, HiddenInput

from crispy_forms.helper import FormHelper

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
        fields = ("title",)


class TopicCommentCreateForm(ModelForm):
    class Meta:
        model = TopicComment
        fields = ("body",)
        widgets = {
        "body": forms.Textarea(attrs = {
            "class": "form-control",
            "label": "",
            "placeholder": "Add new message", 
            "maxLength":"250", 
        }), 
    }


class SearchForumForm(forms.Form):
    query = forms.CharField(max_length=150, label="ForuSEARCH ALL FORUMS")

    def __init__(self, *args, **kwargs):
        super(SearchForumForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "search_forum"
        self.helper.form_class = "form"
