from django.db import models
from django.utils import timezone

class Post(models.Model):
    #link to another table eg. users.
    author = models.ForeignKey('auth.User')
    #define length of post title.
    title = models.CharField(max_length=200)
    #define lenth of post content.
    text = models.TextField()
    #setting created date to current time.
    created_date = models.DateTimeField (    
        default = timezone.now)
    #allows published date to be set to null.
    published_date = models.DateTimeField (
        blank=True, null=True)
    #defines a publish method (function in class is called a method.)
    def publish(self):
      self.published_date = timezone.now()
      self.save()
    #returns string version of post. 
    def __str__(self):
        return self.title