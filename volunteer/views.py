from django.db.models import Q
from django.shortcuts import render
from django.contrib import messages
from django.views.generic import TemplateView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect, HttpRequest

from .forms import VolunteerApplicationForm
from .models import VolunteerApplication, VolunteerJob


class JobListingView(ListView):
    queryset = VolunteerJob.objects.all()
    template_name = "volunteer/jobs_listing.html"

    def get_queryset(self, *args, **kwargs):
        q_set = VolunteerJob.objects.all()
        query = self.request.GET.get("q", None)
        if query is not None:
            q_set = q_set.filter(
            Q(title__icontains = query) |
            Q(hours__icontains = query) |
            Q(location__icontains = query))
        return q_set


class VolunteerApplicationFormView(CreateView):
    model = VolunteerApplication
    template_name = "volunteer/job_apply.html"
    success_url = reverse_lazy("job_listing")
    fields = ["first_name", "last_name","about_you", "email", "contact_number" ]

    def get_context_data(self, **kwargs):
        context = super(VolunteerApplicationFormView, self).get_context_data(**kwargs)
        context["form"] = VolunteerApplicationForm()
        url = self.request.path_info
        job_id = url.replace("volunteer/apply/", "").replace("/", "")
        context["current_job"] = VolunteerJob.objects.get(id=job_id)
        self.request.session["current_job_id"] = job_id
        return context

    def form_valid(self, form):
        form.instance.job = VolunteerJob.objects.get(id=self.request.session["current_job_id"])
        self.object = form.save()
        return HttpResponseRedirect(reverse("volunteer:jobs_listing"))

    def form_invalid(self, form):
        messages.warning(self.request, 'Something went wrong!  Please try again')
        return HttpResponseRedirect(reverse("volunteer:jobs_listing"))
