from django.utils import timezone
from .models import Post, Artist, Album
from .forms import PostForm, ArtistForm, AlbumForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView


class PostListView(ListView): 
    # Automatically gets template file from .lower + .append _html
    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')


class PostDetailView(DetailView):

    model = Post


class PostCreateView(CreateView):

    model = Post
    form_class = PostForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.published_date = timezone.now()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post_detail', args=[self.object.pk])


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


class ArtistListView(ListView):

    template_name = 'blog/artist_list.html'
    model = Artist


class ArtistCreateView(CreateView):

    model = Artist
    form_class = ArtistForm

    def get_success_url(self):
        return reverse('artist_list')


def artist_edit(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    if request.method == "POST":
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm(instance=artist)
    return render(request, 'blog/artist_edit.html', {'form': form})


class ArtistDetailView(DetailView):

    model = Artist


"""

artist.album_set.all()

def album_list(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    albums = Album.objects.filter(artist = artist)
    return render(request, 'blog/album_list.html', {'albums' : albums})
"""

class AlbumCreateView(CreateView):

    model = Album
    form_class = AlbumForm

    def get_success_url(self):
        return reverse('album_list', args=[self.object.artist.pk])


def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            album = form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    return render(request, 'blog/album_edit.html', {'form': form})
