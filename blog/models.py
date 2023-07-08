from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    # ForeignKey relationship with the User model for the author of the post
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # CharField for the title of the post
    title = models.CharField(max_length=200)
    # TextField for the main content of the post
    text = models.TextField()
    # DateTimeField for the creation date of the post
    created_date = models.DateTimeField(default=timezone.now)
    # DateTimeField for the publication date of the post (can be blank and null)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        # Method to set the published_date field to the current time and save the post
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        # Method to return a string representation of the post (title)
        return self.title