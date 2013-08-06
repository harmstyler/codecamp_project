from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>\d+)/$', views.detailID, name='speaker_detail_id'),
    url(r'^(?P<slug>[-\w\d]+),(?P<id>\d+)/$', views.detail, name='speaker_detail'),
)
