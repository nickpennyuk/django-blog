import factory
from blog.models import Post, Artist, Album
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory): # Called in PostFactory

    class Meta:
        model = User


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    author = factory.SubFactory(UserFactory)
    

class ArtistFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Artist


class AlbumFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Album
