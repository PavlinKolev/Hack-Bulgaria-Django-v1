from django.conf.urls import url
from storage import views

app_name = "storage"

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^user-detail/(?P<user_id>[-a-z0-9]+)/$', views.user_detail, name="user_detail"),
    url(r'^add-key/(?P<user_id>[-a-z0-9]+)/$', views.add_key, name="add_key"),
]
