import datetime
from django.shortcuts import render, redirect, get_object_or_404

from django.views.generic import TemplateView
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView

from .models import Image, ImageVote, Comment, CommentVote


class HomeView(TemplateView):
    template_name = "vote/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["day"] = "holmes"
        return context


class ImageDeleteView(DeleteView):
    model = Image
    success_url = "vote:home"


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = "vote:home"


class ImageUpVoteView(View):
    def post(self, request, *args, **kwargs):
        image = get_object_or_404(Image, id=self.kwargs.get("pk"))

        try:
            image_vote = ImageVote.objects.objects.get(user=self.request.user, 
            image=image)
            image_vote.vote = UPVOTE
            image_vote.save()
        except ImageVote.DoesNotExist:
            _= ImageVote.objects.create(
                image=image, 
                user=self.request.user,
                vote=UPVOTE
            )


class ImageDownVoteView(View):
    pass


class CommentUpVoteView(View):
    pass

class CommentDownVoteView(View):
    pass
