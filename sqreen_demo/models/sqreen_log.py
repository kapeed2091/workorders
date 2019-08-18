from django.db import models
from task_management.models import AbstractDateTime


class SqreenLog(AbstractDateTime):
    data = models.TextField()

    @classmethod
    def create(cls, data):
        log = cls.objects.create(data=data)
        return {'log_id': log.id}
