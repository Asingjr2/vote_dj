from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView, CreateView

from .forms import ApplicationForm
from .models import Animal, Application

# Create your views here.
class AdoptFormView(TemplateView):
    template_name = "adopt/adopt_form.html"

    def get_context_data(self, **kwargs):
        context = super(AdoptFormView, self).get_context_data(**kwargs)
        context["form"] = ApplicationForm()
        return context


class AnimalListing(ListView):
    template_name = "adopt/animal_listing.html"
    queryset = Animal.objects.all()

    def get_queryset(self, *args, **kwargs):
        q_set = Animal.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            q_set = q_set.filter(
            Q(name__icontains = query) |
            Q(animal_type__icontains = query) |
            Q(breed__icontains = query) |
            Q(description__icontains = query))
        return q_set

    def get_context_data(self, **kwargs):
        context = super(AnimalListing, self).get_context_data(**kwargs)
        context["all"] = Animal.objects.all().count()
        return context


class DogListing(ListView):
    template_name = "adopt/animal_listing.html"
    queryset = Animal.objects.filter(animal_type="dog")

    def get_context_data(self, **kwargs):
        context = super(DogListing, self).get_context_data(**kwargs)
        context["dogs"] = Animal.objects.filter(animal_type="dog").count()
        return context


class CatListing(ListView):
    template_name = "adopt/animal_listing.html"
    queryset = Animal.objects.filter(animal_type="cat")

    def get_context_data(self, **kwargs):
        context = super(CatListing, self).get_context_data(**kwargs)
        context["cats"] = Animal.objects.filter(animal_type="cat").count()
        return context


class OtherAnimalListing(ListView):
    template_name = "adopt/animal_listing.html"
    queryset = Animal.objects.filter(animal_type="other")

    def get_context_data(self, **kwargs):
        context = super(OtherAnimalListing, self).get_context_data(**kwargs)
        context["other"] = Animal.objects.filter(animal_type="other").count()
        return context


