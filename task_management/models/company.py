from django.db import models
from task_management.models import AbstractDateTime


class Company(AbstractDateTime):
    name = models.CharField(max_length=200, unique=True)

    class Meta:
        app_label = 'task_management'

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

