import pytest
from django.core.urlresolvers import reverse
from .factories import PostFactory

@pytest.mark.django_db # tells pytest-django to use a temporary database
def test_post_list(client):
	url = reverse('post_list')
	response = client.get(url)
	assert 200 == response.status_code

@pytest.mark.django_db
def test_post_detail(client):
	post = PostFactory()
	url = reverse('post_detail', args=[post.pk])
	response = client.get(url)
	assert 200 == response.status_code

@pytest.mark.django_db
def test_post_new(client):
	post = PostFactory()
	url = reverse('post_new')
	response = client.get(url)
	assert 200 == response.status_code
