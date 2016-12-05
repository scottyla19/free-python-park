from django.conf.urls import url

from . import views

app_name = 'header'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api', views.api, name='api'),
]