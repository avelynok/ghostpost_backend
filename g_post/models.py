from django.db import models
from django.utils import timezone

"""
Boolean to tell whether it's a boast or a roast
CharField to put the content of the post in
IntegerField for up votes
IntegerField for down votes
DateTimeField for submission time
"""
# Create your models here.
class Post(models.Model):
    post_title = models.CharField(max_length=30)
    post = models.CharField(max_length=280)
    post_type = models.BooleanField(default=False, help_text="Checked if Boast")
    upVote = models.IntegerField(default=0)
    downVote = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
 
    def __str__(self):
        return self.post