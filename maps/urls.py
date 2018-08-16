from django.urls import path

from . import views
from .views import MapHomeView, ParkView

urlpatterns = [
    path("", MapHomeView.as_view(), name="locations_home"),
    path("parks", ParkView.as_view(), name="parks"),
] 
