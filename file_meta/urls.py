from django.conf.urls import url

from . import views

app_name = 'file_meta'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/(?P<data>.+)$', views.api, name='api'),
]