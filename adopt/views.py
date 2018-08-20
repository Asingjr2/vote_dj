from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, CreateView

from .forms import ApplicationForm

# Create your views here.
class AdoptFormView(TemplateView):
    template_name = "adopt/adopt_form.html"

    def get_context_data(self, **kwargs):
        context = super(AdoptFormView, self).get_context_data(**kwargs)
        context["form"] = ApplicationForm()
        return context


class FormCompleteView(TemplateView):
    template_name = "adopt/form_complete"
