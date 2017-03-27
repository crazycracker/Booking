#!python
# log/urls.py
from django.conf.urls import url
from . import views
# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<block_name>\w+)/classrooms$',views.display, name='classrooms'),
    url(r'^cc1/(?P<room_number>\w+)$',views.cc1,name='cc1'),
    url(r'^register/$',views.registration_form,name='register'),
    url(r'^eventlist$',views.eventlist,name='eventlist')
]
