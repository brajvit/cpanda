from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', ProductListView.as_view(), name=' donate'),
    #url(r'^enquiry/$', 'django_messages.views.enquiry', name='enquiry'),
    #url(r'^enquiry/(?P<recipient>[\w.@+-]+)/$', enquiry, name='messages_compose_to'),
    #url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    url(r'^host/$', views.list, name='list'),
    url(r'^list/(?P<pk>[0-9]+)/$', views.post_detail_list, name='post_detail_list'),
    url(r'^list/detail/$', views.list_detail, name='list_detail'),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.post_edit_list, name='post_edit_list'), 

    url(r'^producthistory/$', ' donate.views.post_history', name='post_history'),
    url(r'^detail/product/(?P<pk>[0-9]+)/$', ' donate.views.post_detail_history', name='post_detail_history'),
    #service
    # url(r'^service/enquiry/$', 'django_messages.views.enquiry', name='enquiry'),
    #url(r'^service/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),
    url(r'^servicehistory/$', ' donate.views.service_history', name='service_history'),
    url(r'^servicelist/$', ' donate.views.servicelist', name='servicelist'),    
    url(r'^detail/service/(?P<pk>[0-9]+)/$', ' donate.views.service_detail_history', name='service_detail_history'),
    url(r'^service/(?P<pk>[0-9]+)/$', ' donate.views.service_detail_home', name='service_detail_home'),
    url(r'^servicehistory/$', ' donate.views.service_history', name='service_history'),
    url(r'^service/(?P<pk>[0-9]+)/edit/$', ' donate.views.post_edit_service', name='post_edit_service'),
    url(r'^offer/service/$', ' donate.views.service', name='service'),
    url(r'^offer/service/(?P<pk>[0-9]+)/$', ' donate.views.post_detail_service', name='post_detail_service'),
    # event    
    #url(r'^event/enquiry/$', 'django_messages.views.enquiry', name='enquiry'),
    #url(r'^event/enquiry/(?P<recipient>[\w.@+-]+)/$', 'django_messages.views.enquiry', name='messages_compose_to'),
    url(r'^events/$', ' donate.views.event', name='event'), 
    url(r'^event/(?P<pk>[0-9]+)/$', ' donate.views.event_detail', name='event_detail'),  
    url(r'^eventhistory/$', ' donate.views.devent_detail', name='devent_detail'),
    url(r'^detail/event/(?P<pk>[0-9]+)/$', ' donate.views.uevent_detail', name='uevent_detail'),
    url(r'^event/edit/(?P<pk>[0-9]+)/$', ' donate.views.devent_edit', name='devent_edit'),
    url(r'^host/event/$', ' donate.views.devent', name='devent'),
    url(r'^host/event/(?P<pk>[0-9]+)/$', ' donate.views.event_detail', name='event_detail'),
    url(r'^event/detail/(?P<pk>[0-9]+)/$', ' donate.views.uevent_detail', name='uevent_detail'),
]
