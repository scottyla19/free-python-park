from django.conf.urls import url

from . import views

app_name = 'shorturl'
#TODO add url to visit sites and take in id_str
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/(?P<new_url>.+)/$', views.api, name='api'),
]