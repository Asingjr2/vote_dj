from django.urls import path

from .views import ForumListAPIView

urlpatterns = [
    path("all_forums/", ForumListAPIView.as_view(), name="all_messages"),
]
