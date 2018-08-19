from django.urls import path

from . import views
from .views import (
    ForumDetailView, 
    ForumCreateView, 
    ForumUpdateView,
    ForumListView,
    ForumDeleteView,

    TopicDetailView, 
    TopicCreateView,
    TopicUpvoteView,
    TopicDownvoteView,

    TopicCommentDetailView, 
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
    path('<slug:slug>/update/',
         ForumUpdateView.as_view(),
         name='forum_moderators_add'),
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
    path('topics/<uuid:pk>/upvote/',
         TopicUpvoteView.as_view(),
         name='topic_upvote'),
    path('topics/<uuid:pk>/downvote/',
         TopicDownvoteView.as_view(),
         name='topic_downvote'),

    # TopicComment urls
    path('<slug:forum_slug>/<uuid:topic_id>/<slug:topic_slug>/<uuid:topic_comment_id>/',
         TopicCommentDetailView.as_view(),
         name='topic_comment_detail'),
    path('comment/comment_create/',
         TopicCommentCreateView.as_view(),
         name='topic_comment_create'),
]
