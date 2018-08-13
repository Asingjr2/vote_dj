from django.urls import path

from . import views
from .views import MapHomeView

urlpatterns = [
    path("", MapHomeView.as_view(), name="locations_home"),
] 
