from django.db import models
from task_management.models import AbstractDateTime


class Order(AbstractDateTime):
    title = models.CharField(max_length=100)
    description = models.TextField()
    deadline = models.DateField()
    workers = models.ManyToManyField('task_management.Worker',
                                     through='task_management.OrderWorker')

    class Meta:
        app_label = 'task_management'

    @classmethod
    def create(cls, title, description, deadline):
        order = cls.objects.create(
            title=title, description=description, deadline=deadline)
        return order.id

    @classmethod
    def assign_worker(cls, order_id, worker_id):
        from task_management.models import OrderWorker
        OrderWorker.create(order_id=order_id, worker_id=worker_id)
        return
