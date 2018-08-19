from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView, CreateView


# Create your views here.
class AdoptFormView(TemplateView):
    template_name = "adopt/adopt_form.html"



class FormCompleteView(TemplateView):
    template_name = "adopt/form_complete"
