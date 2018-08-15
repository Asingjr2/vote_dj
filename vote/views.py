import datetime
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.views.generic import TemplateView
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView

from .models import Image, ImageVote, Comment, CommentVote, UPVOTE, DOWNVOTE


class HomeView(TemplateView):
    template_name = "vote/test.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["day"] = "holmes"
        context["image"] = Image.objects.last()
        context["comment"] = Comment.objects.last()
        return context


class ImageDetailView(DetailView):
    model = Image
    pk_url_kwarg = 'pk'


class ImageDeleteView(DeleteView):
    model = Image
    # lookup_field = "pk"
    success_url = reverse_lazy("home")


class ImageUpvoteView(View):
    def post(self, request, *args, **kwargs):
        image = get_object_or_404(Image, id=self.kwargs.get("pk"))

        try:
            image_vote = ImageVote.objects.get(user=self.request.user, 
            image=image)
            image_vote.vote = UPVOTE
            image_vote.save()
            print("success")
        except ImageVote.DoesNotExist:
            print("failure")
            _= ImageVote.objects.create(
                image=image, 
                user=self.request.user,
                vote=UPVOTE
            )
        return redirect("home")

    
class ImageDownvoteView(View):
    def post(self, request, *args, **kwargs):
        image = get_object_or_404(Image, id=self.kwargs.get("pk"))

        try:
            image_vote = ImageVote.objects.get(user=self.request.user, 
            image=image)
            image_vote.vote = DOWNVOTE
            image_vote.save()
            print("success")
        except ImageVote.DoesNotExist:
            print("failure")
            _= ImageVote.objects.create(
                image=image, 
                user=self.request.user,
                vote=UPVOTE
            )
        return redirect("home")

    
class CommentDetailView(DetailView):
    model = Comment


class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("home")


class CommentUpvoteView(View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs.get("pk"))

        try:
            comment_vote = CommentVote.objects.get(user=self.request.user, 
            comment=comment)
            comment_vote.vote = UPVOTE
            comment_vote.save()
            print("success")
        except CommentVote.DoesNotExist:
            print("failure")
            _= CommentVote.objects.create(
                comment=comment, 
                user=self.request.user,
                vote=UPVOTE
            )
        return redirect("home")

    
class CommentDownvoteView(View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, id=self.kwargs.get("pk"))

        try:
            comment_vote = CommentVote.objects.get(user=self.request.user, 
            comment=comment)
            comment_vote.vote = DOWNVOTE
            comment_vote.save()
            print("success")
        except CommentVote.DoesNotExist:
            print("failure")
            _= CommentVote.objects.create(
                comment=comment, 
                user=self.request.user,
                vote=UPVOTE
            )
        return redirect("home")
