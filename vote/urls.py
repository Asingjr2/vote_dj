from django.urls import path

from . import views
from .views import (
    HomeView,
    ImageDetailView,
    ImageUpvoteView,
    ImageDownvoteView,
    ImageDeleteView,
    CommentDetailView,
    CommentUpvoteView,
    CommentDownvoteView,
    CommentDeleteView,
)

# app_name = "vote"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    # Detail
    path("image/<uuid:pk>", ImageDetailView.as_view(), name="image_detail"),
    path("comment/<uuid:pk>", CommentDetailView.as_view(), name="comment_detail"),
    # Upvote
    path("vote/image/<uuid:pk>", ImageUpvoteView.as_view(), name="image_upvote"),
    path("vote/comment/<uuid:pk>", CommentUpvoteView.as_view(), name="comment_upvote"),
    # Downvote   
    path("downvote/image/<uuid:pk>", ImageDownvoteView.as_view(), name="image_downvote"),
    path("downvote/comment/<uuid:pk>", CommentDownvoteView.as_view(), name="comment_downvote"),
    # Delete
    path("image/delete/<uuid:pk>", ImageDeleteView.as_view(), name="image_delete"),
    path("comment/delete/<uuid:pk>", CommentDeleteView.as_view(), name="comment_delete"),
]
