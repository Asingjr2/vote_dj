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
        context["dogs"] = Animal.objects.filter(animal_type="dog").count()
        context["cats"] = Animal.objects.filter(animal_type="cat").count()
        context["other"] = Animal.objects.filter(animal_type="other").count()
        return context


class DogListing(ListView):
    template_name = "adopt/animal_listing.html"
    queryset = Animal.objects.filter(animal_type="dog")

    def get_context_data(self, **kwargs):
        context = super(DogListing, self).get_context_data(**kwargs)
        context["all"] = Animal.objects.all().count()
        context["dogs"] = Animal.objects.filter(animal_type="dog").count()
        context["cats"] = Animal.objects.filter(animal_type="cat").count()
        context["other"] = Animal.objects.filter(animal_type="other").count()
        return context


class CatListing(ListView):
    template_name = "adopt/animal_listing.html"
    queryset = Animal.objects.filter(animal_type="cat")

    def get_context_data(self, **kwargs):
        context = super(CatListing, self).get_context_data(**kwargs)
        context["all"] = Animal.objects.all().count()
        context["dogs"] = Animal.objects.filter(animal_type="dog").count()
        context["cats"] = Animal.objects.filter(animal_type="cat").count()
        context["other"] = Animal.objects.filter(animal_type="other").count()
        return context


class OtherAnimalListing(ListView):
    template_name = "adopt/animal_listing.html"
    queryset = Animal.objects.filter(animal_type="other")

    def get_context_data(self, **kwargs):
        context = super(OtherAnimalListing, self).get_context_data(**kwargs)
        context["all"] = Animal.objects.all().count()
        context["dogs"] = Animal.objects.filter(animal_type="dog").count()
        context["cats"] = Animal.objects.filter(animal_type="cat").count()
        context["other"] = Animal.objects.filter(animal_type="other").count()
        return context


class AdoptFormView(CreateView):
    template_name = "adopt/adopt_form.html"
    model = Application
    success_url = reverse_lazy("adopt:adopt_all")
    form_class = ApplicationForm
    # fields = ["first_name", "last_name","street_address", "street_address_2", "family_size", "pets_doemail", "contact_number" ]

    def get_context_data(self, **kwargs):
        context = super(AdoptFormView, self).get_context_data(**kwargs)
        context["form"] = ApplicationForm(self.request.POST or None)
        url = self.request.path_info
        pet_id = url.replace("adopt/adopt_form/", "").replace("/", "")
        self.request.session["current_pet_id"] = pet_id
        context["pet_name"] = Animal.objects.get(id=pet_id).name
        context["pet_id"] = self.request.session["current_pet_id"] 
        # context["form2"] = ApplicationForm(self.request.POST)
        return context

    def form_valid(self, form):
        form.instance.pet = Animal.objects.get(id=self.request.session["current_pet_id"])
        self.object = form.save()
        return HttpResponseRedirect(reverse_lazy("adopt:adopt_all"))
    
    def form_invalid(self, form):
        print("something happened", form.non_field_errors)
        if "first_name" in form.errors:
            messages.warning(self.request, 'First name must be between 1 and 50 characters')
        if "last_name" in form.errors:
            messages.warning(self.request, 'Last name must be between 1 and 50 characters')
        if "street_address" in form.errors:
            messages.warning(self.request, 'Street address line 1 must be between 5 and 250 characters')
        if "street_address_2" in form.errors:
            messages.warning(self.request, 'Steert address line 2 must be between 5 and 250 characters')
        if "state" in form.errors:
            messages.warning(self.request, 'State must be between 2 characters')
        if "family_size" in form.errors:
            messages.warning(self.request, 'Family size must be be between 1 and 10')
        if "pets_dogs" in form.errors:
            messages.warning(self.request, 'Number of dogs must be between 0 and 5')
        if "pets_cats" in form.errors:
            messages.warning(self.request, 'Number of cats must be between 0 and 4')
        if "pets_other" in form.errors:
            messages.warning(self.request, 'Number of dogs must be between 0 and 5')
        if "interest_reason" in form.errors:
            messages.warning(self.request, 'Reason for interest must be between 5 and 250 characters')
        if "email" in form.errors:
            messages.warning(self.request, 'Must be valid email')
        if "contact_number" in form.errors:
            messages.warning(self.request, 'Contact number must be 10 digits')
        form2 = ApplicationForm(self.request.POST)
        context = {
            "form":form2
        }
        return render(self.request, "adopt/adopt_form.html", context)
