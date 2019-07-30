from django.db import models
from django.conf import settings


class Friendship(models.Model):
    request_owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    request_target = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='+')

    def __str__(self):
        return f"from {self.request_owner} to user with id {self.request_target}"
