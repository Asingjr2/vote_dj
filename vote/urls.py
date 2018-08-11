from django.urls import path

from . import views
from .views import HomeView, ImageDeleteView, CommentDeleteView, ImageUpvoteView

# app_name = "vote"
urlpatterns = [
    path("", HomeView.as_view(), name="home"), 
    path("image/delete/<uuid:pk>", ImageDeleteView.as_view(), name="image_delete"),
    path("comment/delete/<uuid:pk>", CommentDeleteView.as_view(), name="comment_delete"),
    path("vote/image/<uuid:pk>", ImageUpvoteView.as_view(), name="image_upvote"),
]
