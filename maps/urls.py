from django.urls import path

from . import views
from .views import MapHomeView, ParkView

app_name = "locations"
urlpatterns = [
    path("", MapHomeView.as_view(), name="home"),
    path("parks", ParkView.as_view(), name="parks"),
] 
