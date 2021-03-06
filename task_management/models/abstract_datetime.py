from django.db import models


class AbstractDateTime(models.Model):
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_update_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
