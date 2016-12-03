from django.conf.urls import url

from . import views

app_name = 'timestamp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<param_str>[\w\-\/\s]+)/$', views.api, name='api'),
]