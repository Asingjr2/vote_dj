from django.urls import path

from . import views
from .views import (
    HomeView,
    ImageDetailView,
    ImageUpvoteView,
    ImageDownvoteView,
    ImageDeleteView,
    ContactUsView,
    # VolunteerView,

    ########333
    TestView
)

urlpatterns = [


    #######TEST
    path("test", TestView.as_view(), name="test"),

    #######

    path("main", HomeView.as_view(), name="home"),
    path("image/<uuid:pk>", ImageDetailView.as_view(), name="image_detail"),
    path("vote/image/<uuid:pk>", ImageUpvoteView.as_view(), name="image_upvote"),
    path("downvote/image/<uuid:pk>", ImageDownvoteView.as_view(), name="image_downvote"),
    path("image/delete/<uuid:pk>", ImageDeleteView.as_view(), name="image_delete"),
    path("contact/", ContactUsView.as_view(), name="contact_us"),
]
