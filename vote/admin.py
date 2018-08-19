from django.contrib import admin

from .models import Image, ImageVote, Recommendation


admin.site.register(Image)
admin.site.register(ImageVote)
admin.site.register(Recommendation)
