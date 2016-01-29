import pytest
from django.core.urlresolvers import reverse
from .factories import PostFactory, ArtistFactory, AlbumFactory
from blog.models import Artist, Post, Album

@pytest.mark.django_db # tells pytest-django to use a temporary database
def test_post_list(client):
    url = reverse('post_list') # Reverse turns url "name" back to url format and assigns it to url variable
    response = client.get(url) # assigns response to url variable
    assert 200 == response.status_code

@pytest.mark.django_db
def test_post_detail(client):
    post = PostFactory()
    url = reverse('post_detail', args=[post.pk])
    response = client.get(url)
    assert 200 == response.status_code

@pytest.mark.django_db
def test_post_new(client):
    url = reverse('post_new')
    response = client.get(url)
    assert 200 == response.status_code

"""
@pytest.mark.dajngo_db
def test_create_post(client):
    url = reverse('post_new')
    data = {
    'title' : 'Post Test Post',
    'text' : 'Test Post Text',
    }
    response = client.post(url, data)
    assert 302 == response.status_code
    post = Post.objects.first()
    assert 'Post Test Post' == post.title
    assert 'Test Post Text' == post.text
"""

@pytest.mark.django_db
def test_post_edit(client):
    post = PostFactory()
    url = reverse('post_edit', args=[post.pk])
    response = client.get(url)
    assert 200 == response.status_code

@pytest.mark.django_db
def test_artist_list(client):
    url = reverse('artist_list')
    response = client.get(url)
    assert 200 == response.status_code

@pytest.mark.django_db
def test_artist_new(client):
    url = reverse('artist_new')
    response = client.get(url)
    assert 200 == response.status_code

@pytest.mark.django_db
def test_artist_new_post(client):
    url = reverse('artist_new')
    data = {'name': 'Nick'}
    response = client.post(url, data)
    assert 302 == response.status_code
    artist = Artist.objects.first()
    assert 'Nick' == artist.name

@pytest.mark.django_db
def test_artist_edit(client):
    artist = ArtistFactory()
    url = reverse('artist_edit', args=[artist.pk])
    response = client.get(url)
    assert 200 == response.status_code

@pytest.mark.django_db
def test_album_list(client):
    artist = ArtistFactory()
    url = reverse('album_list', args=[artist.pk])
    response = client.get(url)
    assert 200 == response.status_code

@pytest.mark.django_db
def test_album_new(client):
    url = reverse('album_new')
    response = client.get(url)
    assert 200 == response.status_code


@pytest.mark.django_db
def test_album_new_post(client):
    artist = ArtistFactory()
    url = reverse('album_new')
    data = {
    'artist' : artist.pk,
    'title' : 'Last Resort',
    'year' : '11/11/2011'
    }
    response = client.post(url, data)
    assert 302 == response.status_code
    album = Album.objects.first()
    assert 'Last Resort' == album.title
    assert '11/11/2011' == album.year


@pytest.mark.django_db
def test_album_edit(client):
    album = AlbumFactory()
    url = reverse('album_edit', args=[album.pk])
    response = client.get(url)
    assert 200 == response.status_code
