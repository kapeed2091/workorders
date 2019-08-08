from django.conf.urls import url

from task_management.views.create_worker import create_worker
from task_management.views.delete_worker import delete_worker
from task_management.views.create_work_order import create_work_order


urlpatterns = [
    url(r'^create-worker/$', create_worker),
    url(r'^delete-worker/$', delete_worker),
    url(r'^create-work-order/$', create_work_order),
]
