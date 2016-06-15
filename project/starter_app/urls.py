from django.conf.urls import url
from . import views


app_name = 'starter_app'

urlpatterns = [
	url(r'^$', views.show_posts, name='posts'),
	url(r'^posts/(?P<pk>\d+)$', views.post_detail, name='post_detail'),
	url(r'^create-new-post/$', views.create_new_post, name='create_new_post'),
	url(r'^update-post/(?P<pk>\d+)$', views.EditPost.as_view(), name='edit-post'),
]
