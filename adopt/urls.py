from django.urls import path

from . import views
from .views import AdoptFormView, FormCompleteView


app_name = "adopt"
urlpatterns = [
    path("", AdoptFormView.as_view(), name="adopt_form"),
    path("form_complete", FormCompleteView.as_view(), name="form_complete")
]
