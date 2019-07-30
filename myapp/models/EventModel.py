from django.db import models
from django.contrib.postgres.fields import JSONField
from django.conf import settings


class Event(models.Model):
    title = models.CharField(max_length=64, blank=False)
    text = models.TextField(blank=False)
    coordinates = JSONField(default=dict, blank=True)

    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='members', blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)

    date = models.DateTimeField()

    def __str__(self):
        return self.title
