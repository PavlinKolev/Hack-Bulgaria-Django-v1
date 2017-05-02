from django.conf.urls import url
from website import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blogs/detail/(?P<blog_id>[0-9]+)/$', views.detail, name='detail_post'),
    url(r'^blogs/add/$', views.create_blog, name='create_blog')
]
