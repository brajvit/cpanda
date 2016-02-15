from django.conf.urls import patterns, include, url

urlpatterns = patterns('events.views',
    url(r'^$', 'event', name='event'),
    url(r'^event/(?P<pk>[0-9]+)/$', 'event_detail', name='event_detail'),
    url(r'^host/$', 'host', name='host'),
    url(r'^detail/(?P<pk>[0-9]+)/$', 'host_detail', name='host_detail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', 'host_edit', name='host_edit'),
)
