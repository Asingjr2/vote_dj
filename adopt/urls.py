from django.urls import path

from . import views
from .views import AdoptHomeView, AdoptFormView, AnimalListing, DogListing, CatListing, OtherAnimalListing


app_name = "adopt"
urlpatterns = [
    path("", AdoptHomeView.as_view(), name="home"),
    path("all", AnimalListing.as_view(), name="adopt_all"),
    path("dogs", DogListing.as_view(), name="adopt_dogs"),
    path("cats", CatListing.as_view(), name="adopt_cats"),
    path("other", OtherAnimalListing.as_view(), name="adopt_other"),
    path("adopt_form/<uuid:pk>", AdoptFormView.as_view(), name="adopt_form"),
]
