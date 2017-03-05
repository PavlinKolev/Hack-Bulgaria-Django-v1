from django.conf.urls import url, include
from storage import views


urlpatterns = [
    url(r'^create-user/$', views.create_user, name='create_user'),
    url(r'^(?P<user_id>[-a-z0-9]+)/$', views.set_user_data, name='set_user_data'),
    url(r'^(?P<user_id>[-a-z0-9]+)/(?P<key>[A-za-z0-9]+)/$', views.user_data_by_key, name='user_data_by_key')
]
