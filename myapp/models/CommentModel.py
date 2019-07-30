from django.db import models
from django.conf import settings

from myapp.models.EventModel import Event


class Comment(models.Model):
    text = models.CharField(max_length=128, blank=False)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    is_tread = models.BooleanField(default=False)

    def __str__(self):
        return self.text
