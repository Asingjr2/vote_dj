from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator

from base.models import BaseModel


UPVOTE = 1
DOWNVOTE = -1
VOTE_CHOICES = (
    (UPVOTE, "+1"), 
    (DOWNVOTE, "-1")
)


class Recommendation(BaseModel):
    subject = models.CharField(max_length=100)
    body = models.CharField(max_length=250)
    email = models.EmailField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return "Comment subject: {}".format(self.subject)

    class Meta:
        verbose_name = "message"
        

class Image(BaseModel):
    image_name = models.CharField(max_length=100)
    url = models.CharField(max_length=150, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "This is image {}".format(self.image_name)

    @property
    def upvotes(self):
        return self.imagevote.filter(vote=UPVOTE).count()

    @property
    def downvotes(self):
        return self.imagevote.filter(vote=DOWNVOTE).count()

    @property
    def score(self):
        return self.imagevote.filter(vote=DOWNVOTE).count() + self.imagevote.filter(vote=UPVOTE).count()


class ImageVote(BaseModel):
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="imagevote")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=VOTE_CHOICES, default=UPVOTE)

    class Meta:
        unique_together = (
            ("user", "image")
        )
