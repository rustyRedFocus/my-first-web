from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.borrow_video, name='borrow_video'),
	url(r'^video/(?P<pk>[0-9]+)/$', views.video_detail, name='video_detail'),
	url(r'^video/new/$', views.video_new, name='video_new'),
	url(r'^video/(?P<pk>[0-9]+)/edit/$', views.video_edit, name='video_edit'),
	


]