import pytest
from django.core.urlresolvers import reverse
from .factories import PostFactory, ArtistFactory, AlbumFactory

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
def test_album_edit(client):
        album = AlbumFactory()
        url = reverse('album_edit', args=[album.pk])
        response = client.get(url)
        assert 200 == response.status_code
