import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

from .models import Image, ImageVote,UPVOTE, DOWNVOTE, Recommendation
from adopt.models import Animal
from .forms import RecommendationForm
from messageboard.models import Forum


class HomeView(TemplateView):
    template_name = "vote/adopt.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context["day"] = "holmes"
        context["image"] = Image.objects.last()
        context["animal"] = Animal.objects.get(name="Spike")
        context["animal2"] = Animal.objects.get(name="Tabatha")
        context["animal3"] = Animal.objects.last()
        return context


class ContactUsView(CreateView):
    model = Recommendation
    form_class = RecommendationForm
    succes_url = "/home"
    template_name = "vote/contact.html"

    def form_valid(self, form):
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
