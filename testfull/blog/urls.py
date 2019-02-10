from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^api/v1/blogs/(?P<pk>[0-9]+)$', views.get_delete_update_blog, name='get_delete_update_blog'),
    url(r'^api/v1/blogs/$', views.get_post_blogs, name='get_post_blogs')
]
