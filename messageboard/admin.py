from django.contrib import admin

from .models import (
    Forum,
    Topic,
    TopicComment,
    TopicVote
    )
    
admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(TopicVote)
admin.site.register(TopicComment)
