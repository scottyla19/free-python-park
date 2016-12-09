from django.conf.urls import url

from . import views

app_name = 'shorturl'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/(?P<new_url>.+)/$', views.api, name='api'),
    url(r'^(?P<visit_url>.+)/$', views.visit, name='visit'),

]