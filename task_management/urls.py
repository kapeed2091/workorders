from django.conf.urls import url

from task_management.views.create_worker import create_worker


urlpatterns = [
    url(r'^create-worker/$', create_worker),
]
