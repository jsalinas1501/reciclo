from django.conf.urls import url

from .views import my_list_view, CreateView, DetailView


urlpatterns = [
    url(
        r'^$',
        my_list_view,
        name='can-list',
    ),
    url(
        r'^(?P<pk>[0-9]+)/$',
        DetailView.as_view(),
        name='can-detail',
    ),
    url(
        r'^crear/$',
        CreateView.as_view(),
        name='can-create',
    ),
]
