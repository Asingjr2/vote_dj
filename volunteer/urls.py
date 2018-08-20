from django.urls import path

from . import views
from .views import JobListingView,VolunteerApplicationFormView, VolunteerFormCompleteView


app_name = "volunteer"
urlpatterns = [
    path("", JobListingView.as_view(), name="jobs_listing"),
    path("apply/<uuid:pk>", VolunteerApplicationFormView.as_view(), name="job_apply"),
    path("form_complete", VolunteerFormCompleteView.as_view(), name="form_complete")
]
