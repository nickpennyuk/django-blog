from django.conf.urls import include, url
from . import views
from .forms import PostForm

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^artists/$', views.artist_list, name='artist_list'),
    url(r'^artists/new/$', views.artist_new, name='artist_new'),
    url(r'^artists/(?P<pk>[0-9]+)/edit/$', views.artist_edit, name='artist_edit'),
    url(r'^artists/albums$', views.album_list, name='album_list'),
    url(r'^artists/albums/new/$', views.artist_new, name='album_new'),
    url(r'^artists/(?P<pk>[0-9]+)/albums/edit$', views.artist_edit, name='album_edit'),
]
