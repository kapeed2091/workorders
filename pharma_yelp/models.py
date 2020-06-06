from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class UserRating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user')
    rating = models.IntegerField(default=0)
    comments = models.CharField(max_length=140, default='')
    given_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='given_by')
    approval = models.IntegerField(default=0)
