from django.db.models import Q

from rest_framework import generics

from .serializers import ForumSerializer
from messageboard.models import Forum


class ForumListAPIView(generics.ListAPIView):
    serializer_class = ForumSerializer

    def get_queryset(self, *args, **kwargs):
        """
            Base forum set is all forums in DB.
            Query set allows for search filtering based on user info.
        """
        q_set = Forum.objects.all()
        query = self.request.GET.get("q", None)

        if query is not None:
            q_set = q_set.filter(
                Q(slug__icontains = query) | 
                Q(creator__username__icontains = query)
            )
        return q_set
