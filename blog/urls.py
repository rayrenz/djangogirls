from django.conf.urls import url

from . import views


urlpatterns = [
    # ex: /blog/
    url(r'^$', views.PostListView.as_view(), name='post_list'),
]