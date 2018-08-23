from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ApplicationForm
from .models import Animal, Application

# Create your views here.

class AdoptHomeView(TemplateView):
    template_name = "adopt/adopt_home.html"


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


class AdoptFormView(CreateView):
    template_name = "adopt/adopt_form.html"
    model = Application
    success_url = reverse_lazy("adopt:adopt_all")
    form_class = ApplicationForm
    # fields = ["first_name", "last_name","street_address", "email", "contact_number" ]

    def get_context_data(self, **kwargs):
        context = super(AdoptFormView, self).get_context_data(**kwargs)
        context["form"] = ApplicationForm()
        url = self.request.path_info
        pet_id = url.replace("adopt/adopt_form/", "").replace("/", "")
        self.request.session["current_pet_id"] = pet_id
        context["pet_name"] = Animal.objects.get(id=pet_id).name
        context["pet_id"] = self.request.session["current_pet_id"] 
        return context

    def form_valid(self, form):
        form.instance.pet = Animal.objects.get(id=self.request.session["current_pet_id"])
        self.object = form.save()
        return HttpResponseRedirect(reverse_lazy("adopt:addopt_all"))
    
    def form_invalid(self, form):
        print("something happened", form.non_field_errors)
        messages.warning(self.request, 'Something went wrong!  Please try again')
        return HttpResponseRedirect(reverse_lazy("adopt:adopt_form", args=[self.request.session["current_pet_id"]]))
