from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views import View
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect


from .mixins import ModeratorRequiredMixin
from .forms import ForumUpdateForm, ForumCreateForm, TopicCreateForm,TopicCommentCreateForm, SearchForumForm

from .models import (
    Forum,
    Topic,
    TopicComment,
    TopicVote,
    UPVOTE,
    DOWNVOTE,
)

class ForumDetailView(DetailView):
    model = Forum

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic_form"] = TopicCreateForm()
        return context
    
 
class ForumCreateView(CreateView):
    model = Forum
    fields = ["slug"]
    template_name_suffix = "_create"
    success_url = reverse_lazy("messageboard:forum_list")

    def post(self, request):
        def form_valid(self, form):
            self.object = form.save()
            self.object.moderators.add(self.request.user)
            return HttpResponseRedirect(self.get_success_url())
        
        def form_invalid(self, form):
            print("something happened", form.non_field_errors)
            if "slug" in form.errors:
                messages.warning(self.request, 'Forum name  cannot contain characters')
            return HttpResponseRedirect("/forum_list")


class ForumListView(ListView):
    model = Forum
    queryset = Forum.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = SearchForumForm()
        context["forum_create_form"] = ForumCreateForm()
        return context


class ForumUpdateView(ModeratorRequiredMixin, UpdateView):
    model = Forum
    form_class = ForumUpdateForm

    def get_forum(self):
        return self.get_object()


class ForumDeleteView(DeleteView):
    model = Forum
    success_url = reverse_lazy("forum_list")


class TopicCreateView(View):
    
    def post(self, request):
        form = TopicCreateForm(request.POST)
        if form.is_valid():
            new_topic = Topic.objects.create(
                forum = Forum.objects.get(slug = request.POST["forum_slug"]),
                user = request.user, 
                title = request.POST["title"]
            )
            new_topic.save()
        return HttpResponseRedirect(reverse("forum_detail", args= (request.POST["forum_slug"],)))


class TopicDetailView(DetailView):
    model = Topic
    pk_url_kwarg = 'topic_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["topic_comment_form"] = TopicCommentCreateForm()
        return context


class TopicUpvoteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        topic = get_object_or_404(Topic, id=self.kwargs.get('pk'))

        try:
            topic_vote = TopicVote.objects.get(
                user=self.request.user,
                topic=topic
            )
            topic_vote.vote = UPVOTE
            topic_vote.save()
        except TopicVote.DoesNotExist:
            _ = TopicVote.objects.create(
                user=self.request.user,
                topic=topic,
                vote=UPVOTE
            )
        # Changing redirect to home
        return reverse("forum_list")


class TopicDownvoteView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        topic = get_object_or_404(Topic, id=self.kwargs.get('pk'))

        try:
            topic_vote = TopicVote.objects.get(
                user=self.request.user,
                topic=topic
            )
            topic_vote.vote = DOWNVOTE
            topic_vote.save()
        except TopicVote.DoesNotExist:
            _ = TopicVote.objects.create(
                user=self.request.user,
                topic=topic,
                vote=DOWNVOTE
            )
        return reverse("forum_list")


class TopicCommentCreateView(View):
    
    def post(self, request):
        form = TopicCommentCreateForm(request.POST)
        if form.is_valid():
            new_topic_comment = TopicComment.objects.create(
                topic = Topic.objects.get(id = request.POST["topic_id"]),
                user = request.user, 
                body = request.POST["body"]
             )
            new_topic_comment.save()
            current_topic = Topic.objects.get(id=request.POST["topic_id"])
            print(request.POST["topic_id"])
        return redirect("/messageboard/{}/{}/{}".format(current_topic.forum.slug, current_topic.id,            current_topic.slug,))

        
class TopicCommentDetailView(DetailView):
    model = TopicComment
    pk_url_kwarg = 'topic_comment_id'