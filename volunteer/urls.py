from django.urls import path

from . import views
from .views import JobListingView,VolunteerApplicationFormView


app_name = "volunteer"
urlpatterns = [
    path("", JobListingView.as_view(), name="jobs_listing"),
    path("apply/<uuid:pk>", VolunteerApplicationFormView.as_view(), name="job_apply"),
]
