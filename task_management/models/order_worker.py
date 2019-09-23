from django.db import models
from task_management.models import AbstractDateTime


class OrderWorker(AbstractDateTime):
    order = models.ForeignKey('task_management.Order',
                              on_delete=models.CASCADE)
    worker = models.ForeignKey('task_management.Worker',
                               on_delete=models.CASCADE)

    class Meta:
        app_label = 'task_management'

    @classmethod
    def create(cls, order_id, worker_id):
        from task_management.constants import MAX_WORKERS_FOR_ORDER

        query = cls.objects.filter(order_id=order_id)
        existing_workers = query.count()

        if query.filter(worker_id=worker_id).exists():
            # Handling case where same worker is re-assigned to an order
            raise Exception

        if existing_workers >= MAX_WORKERS_FOR_ORDER:
            # Handling case where order reached max workers assigned to it
            raise Exception
        else:
            cls.objects.create(order_id=order_id, worker_id=worker_id)

        return

    @classmethod
    def fetch_orders(cls, worker_id):
        query = cls.objects.filter(
            worker_id=worker_id).order_by('order__deadline')
        work_orders = []
        for each_item in query:
            work_orders.append({
                'order_id': each_item.order_id,
                'title': each_item.order.title,
                'description': each_item.order.description,
                'deadline': each_item.order.deadline
            })
        return work_orders
