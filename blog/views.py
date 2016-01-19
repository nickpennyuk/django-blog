from django.utils import timezone
from .models import Post, Artist, Album
from .forms import PostForm, ArtistForm, AlbumForm
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView


class PostListView(ListView):

    template_name = 'blog/post_list.html'

    def get_queryset(self):
        return Post.objects.filter(
            published_date__lte=timezone.now()
        ).order_by('-published_date')


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


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
    return render(request, 'blog/post_edit.html', {'form': form})


class ArtistListView(ListView):
    template_name = 'blog/artist_list.html'
    model = Artist


def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save()
            return redirect('artist_list')
    else:
        form = ArtistForm()
    return render(request, 'blog/artist_edit.html', {'form': form})


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


def album_list(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    albums = Album.objects.filter(artist = artist)
    return render(request, 'blog/album_list.html', {'albums' : albums})


def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('album_list', album.artist.pk)
    else:
        form = AlbumForm()
    return render(request, 'blog/album_edit.html', {'form': form})


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
