from django.conf.urls import url

from sqreen_demo.views import webhook


urlpatterns = [
    url(r'^webhook/$', webhook),
]
