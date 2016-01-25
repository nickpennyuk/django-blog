import factory
from blog.models import Post
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = User


class PostFactory(factory.django.DjangoModelFactory):

	class Meta:
		model = Post

	author = factory.SubFactory(UserFactory)