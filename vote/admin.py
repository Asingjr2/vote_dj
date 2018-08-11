from django.contrib import admin

from .models import Image, Comment, ImageVote, CommentVote

# Register your models here.
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(ImageVote)
admin.site.register(CommentVote)
