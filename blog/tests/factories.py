import factory
from datetime import date
from blog.models import Post, Artist, Album
from django.contrib.auth.models import User


TEST_PASSWORD = 'pass'


class UserFactory(factory.django.DjangoModelFactory): # Called in PostFactory

    class Meta:
        model = User

    password = factory.PostGenerationMethodCall('set_password', TEST_PASSWORD)


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

    artist = factory.SubFactory(ArtistFactory)
    year = date.today()
    
