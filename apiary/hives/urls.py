from django.conf.urls import url

from . import views

app_name = "hives"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<inspection_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^hive/(?P<hive_id>[0-9]+)/$', views.list, name='list'),
    url(r'^inspection/(?P<inspection_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^compare/(?P<inspection_id_a>[0-9]+)-(?P<inspection_id_b>[0-9]+)/$', views.compare, name='compare'),
]
