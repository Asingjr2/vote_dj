from django.contrib import admin

from .models import Image, Comment, ImageVote, CommentVote, Recommendation

# Register your models here.
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(ImageVote)
admin.site.register(CommentVote)
admin.site.register(Recommendation)
