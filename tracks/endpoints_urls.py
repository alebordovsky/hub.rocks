from django.conf.urls import patterns, include, url

from tracks.endpoints import (
    TrackListAPIView, VoteAPIView,
    NowPlayingAPIView, NextTrackAPIView)


urlpatterns = patterns('',
    url(r'^tracks/$', TrackListAPIView.as_view(), name='list'),
    url(r'^tracks/(?P<service_id>\d+)/vote/$', VoteAPIView.as_view(), name='vote'),
    
    url(r'^tracks/now-playing/$', NowPlayingAPIView.as_view(), name='now-playing'),
    url(r'^tracks/next/$', NextTrackAPIView.as_view(), name='next'),
)