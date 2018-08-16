import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .models import Image, ImageVote, Comment, CommentVote, UPVOTE, DOWNVOTE, Recommendation
from .forms import RecommendationForm


class HomeView(TemplateView):
    template_name = "vote/adopt.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["day"] = "holmes"
        context["image"] = Image.objects.last()
        context["comment"] = Comment.objects.last()
        return context


class ContactUsView(CreateView):
    model = Recommendation
    form_class = RecommendationForm
    succes_url = "/home"
    template_name = "vote/contact.html"

    def form_valid(self, form):
        print("form looks good")
        # if self.request.user:
            # form.instance.creator = self.request.user
        self.object = form.save()
        return redirect("home")

    def form_invalid(self, form):
        print("something happened", form.non_field_errors)
        if "subject" in form.errors:
            messages.warning(self.request, 'Message subject cannot be blank and must be less than 100 characters')
        if "body" in form.errors:
            messages.warning(self.request, 'Message cannot be blank and must be less than 250 characters')
        if "email" in form.errors:
            messages.warning(self.request, 'Message must include valid email address.')
        return HttpResponseRedirect("/contact")
    

    def get_context_data(self,**kwargs):
        context = super(ContactUsView, self).get_context_data(**kwargs)
        context["form2"] = RecommendationForm
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
