from django.utils.timesince import timesince

from rest_framework import serializers

from messageboard.models import Forum


class ForumSerializer(serializers.ModelSerializer):
    date_display = serializers.SerializerMethodField()
    timesince = serializers.SerializerMethodField()

    class Meta:
        model = Forum
        fields = [
            "slug", 
            "moderators",
            "created_at", 
            "updated_at", 
            "date_display", 
            "timesince"
        ]

    # Additional custom field
    def get_date_display(self, obj):
        return obj.created_at.strftime("%b %d %I: %M %p")

    # Additional custom field
    def get_timesince(self, obj):
        return timesince(obj.created_at) + " ago "
