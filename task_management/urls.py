from django.conf.urls import url

from task_management.views.create_worker import create_worker
from task_management.views.delete_worker import delete_worker
from task_management.views.create_work_order import create_work_order
from task_management.views.assign_worker import assign_worker
from task_management.views.get_work_orders import get_work_orders
from task_management.views.get_workers import get_workers


urlpatterns = [
    url(r'^create-worker/$', create_worker),
    url(r'^delete-worker/$', delete_worker),
    url(r'^create-work-order/$', create_work_order),
    url(r'^assign-worker/$', assign_worker),
    url(r'^get-work-orders/$', get_work_orders),
    url(r'^get-workers/$', get_workers),
]
