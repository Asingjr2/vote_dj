from django.urls import path

from . import views
from .views import (
    HomeView,
    ContactUsView,
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact/", ContactUsView.as_view(), name="contact_us"),
]

