from django.conf.urls import url
from . import views

# blog URL Configuration

urlpatterns = [
    # 1, 2 version
    # url(r'^$', views.post_list, name='post_list'),
    
    # version 3 (class-based views)
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
        r'(?P<post>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
]
