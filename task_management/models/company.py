from django.db import models
from task_management.models import AbstractDateTime


class Company(AbstractDateTime):
    name = models.CharField(max_length=300, unique=True)

    class Meta:
        app_label = 'task_management'
