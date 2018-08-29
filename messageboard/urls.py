from django.urls import path

from . import views
from .views import (
    ForumDetailView, 
    ForumCreateView,
    ForumListView,
    ForumDeleteView,
    TopicDetailView,
    TopicCreateView,
    TopicCommentCreateView,
)

app_name = "messageboard"
urlpatterns = [
    # Forum urls
    path('forum/forum_create',
         ForumCreateView.as_view(),
         name='forum_create'),
    path('',
         ForumListView.as_view(),
         name='forum_list'),
    path('<slug:slug>/',
         ForumDetailView.as_view(),
         name='forum_detail'),
    path('<slug:slug>/forum_delete/',
         ForumDeleteView.as_view(),
         name='forum_delete'),

    # Topic urls
    path('<slug:forum_slug>/<uuid:topic_id>/<slug:topic_slug>/',
         TopicDetailView.as_view(),
         name='topic_detail'),
    path('topic/topic_create/',
         TopicCreateView.as_view(),
         name='topic_create'),
    path('comment/comment_create/',
         TopicCommentCreateView.as_view(),
         name='topic_comment_create'),
]
