from django.conf.urls import url

from . import views

app_name = 'image_search'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^latest', views.latest, name='latest'),
    url(r'^api/(?P<search_str>[\w\-\/\s]+)/$', views.api, name='api'),


]