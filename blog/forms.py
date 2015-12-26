from django import forms
from .models import Post, Artist, Album

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'text',)

class ArtistForm(forms.ModelForm):
	class Meta:
		model = Artist
		fields = ('name',)

class AlbumForm(forms.ModelForm):
	class Meta:
		model = Album
		fields = ('artist', 'title', 'year',)
