from django.conf.urls import include, url
from . import views
from .forms import PostForm

urlpatterns = [

#  Home
    url(r'^$', views.post_list, name='post_list'), # List of all posts on home page
#  Blog
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'), # The individual clicked post
    url(r'^post/new/$', views.post_new, name='post_new'), # New post page
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'), # The edit post page after clicking through to individual post
#  Artist
    url(r'^artist/$', views.artist_list, name='artist_list'), # list of artists
    url(r'^artist/new/$', views.artist_new, name='artist_new'), # add new artist
    url(r'^artist/(?P<pk>[0-9]+)/edit/$', views.artist_edit, name='artist_edit'), # edit artists
#  Album
    url(r'^album/(?P<pk>[0-9]+)/$', views.album_detail, name='album_detail'),
    url(r'^artist/(?P<pk>[0-9]+)/album/$', views.album_list, name='album_list'),
    url(r'^artist/album/new/$', views.album_new, name='album_new'),
]
