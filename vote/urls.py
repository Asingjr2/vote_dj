from django.urls import path

from . import views
from .views import (
    HomeView,
    ImageUpvoteView,
    ImageDownvoteView,
    ContactUsView,
    ########333
    TestView
)

urlpatterns = [


    #######TEST
    path("test", TestView.as_view(), name="test"),

    #######

    path("main", HomeView.as_view(), name="home"),
    path("vote/image/<uuid:pk>", ImageUpvoteView.as_view(), name="image_upvote"),
    path("downvote/image/<uuid:pk>", ImageDownvoteView.as_view(), name="image_downvote"),
    path("contact/", ContactUsView.as_view(), name="contact_us"),
]

