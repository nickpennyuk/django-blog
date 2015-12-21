from django import forms
from .models import Post
from .models import Artist

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('author', 'title', 'text',)

class ArtistForm(forms.ModelForm):
	class Meta:
		model = Artist
		fields = ('name',)