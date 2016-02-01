from django.db import models
from django.utils import timezone
from datetime import date

"""
Class is a special keyword that indicates that we are defining an object.
Post is the name of our model.
models.Model means that the Post is a Django Model, so Django knows that
it should be saved in the database.
"""

class Post(models.Model):
    #link to another table eg. users.
    author = models.ForeignKey('auth.User')
    #define length of post title.
    title = models.CharField(max_length=200)
    #define length of post content.
    text = models.TextField()
    #setting created date to current time.
    created_date = models.DateTimeField (    
        default = timezone.now)
    #allows published date to be set to null.
    published_date = models.DateTimeField (
        blank=True, null=True)
    #defiabout:addonsnes a publish method (function in class is called a method.)
    def publish(self):
      self.published_date = timezone.now()
      self.save()
    #returns string version of post. 
    def __str__(self):
        return self.title

        #hidden id increment blah

class Artist(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=50)
    year = models.DateField(auto_now=False)

    def __str__(self):
        return self.title