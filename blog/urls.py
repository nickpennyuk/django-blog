from django.conf.urls import include, url
from . import views
from .views import PostListView, ArtistListView, PostDetailView, PostCreateView, ArtistCreateView, AlbumCreateView, ArtistDetailView, PostUpdateView, ArtistUpdateView, AlbumUpdateView
from .forms import PostForm

urlpatterns = [

#  Home
    url(r'^$', PostListView.as_view(), name='post_list'), # List of all posts on home page
#  Blog
    url(r'^post/(?P<pk>[0-9]+)/$', PostDetailView.as_view(), name='post_detail'), # The individual clicked post
    url(r'^post/new/$', PostCreateView.as_view() , name='post_new'), # New post page
    url(r'^post/(?P<pk>[0-9]+)/edit/$', PostUpdateView.as_view(), name='post_edit'), # The edit post page after clicking through to individual post
    url(r'^post/(?P<pk>[0-9]+)/remove/$', views.post_remove, name='post_remove'),
#  Artist
    url(r'^artist/$', ArtistListView.as_view(), name='artist_list'), # list of artists
    url(r'^artist/new/$', ArtistCreateView.as_view(), name='artist_new'), # add new artist
    url(r'^artist/(?P<pk>[0-9]+)/edit/$', ArtistUpdateView.as_view(), name='artist_edit'), # edit artists
    url(r'^artist/(?P<pk>[0-9]+)/remove/$', views.artist_remove, name='artist_remove'),
#  Album
    url(r'^artist/(?P<pk>[0-9]+)/album/$', ArtistDetailView.as_view(), name='album_list'),
    url(r'^artist/(?P<pk>[0-9]+)/album/new/$', AlbumCreateView.as_view(), name='album_new'),
    url(r'^artist/album/(?P<pk>[0-9]+)/edit/$', AlbumUpdateView.as_view(), name='album_edit'),

]