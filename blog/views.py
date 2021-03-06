from django.utils import timezone
from .models import Post, Artist, Album
from .forms import PostForm, ArtistForm, AlbumForm
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


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


class PostUpdateView(UpdateView):

    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_detail', args=[self.object.pk])


class PostDeleteView(DeleteView):

    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('post_list', args=[self.object.pk])


"""
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
"""
    """
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
"""


class ArtistListView(ListView):

    template_name = 'blog/artist_list.html'
    model = Artist


class ArtistDetailView(DetailView):

    model = Artist


class ArtistCreateView(CreateView):

    model = Artist
    form_class = ArtistForm

    def get_success_url(self):
        return reverse('artist_list')


class ArtistUpdateView(UpdateView):

    model = Artist
    form_class = ArtistForm

    def get_success_url(self):
        return reverse('artist_list')


def artist_remove(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artist.delete()
    return redirect('artist_list')


class AlbumCreateView(CreateView):

    model = Album
    form_class = AlbumForm

    def _artist(self):
        pk = self.kwargs.get('pk', None)
        artist = get_object_or_404(Artist, pk=pk)
        return artist

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'artist': self._artist(),
        })
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.artist = self._artist()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('album_list', args=[self.object.artist.pk])


class AlbumUpdateView(UpdateView):

    model = Album
    form_class = AlbumForm

    def get_success_url(self):
        return reverse('album_list', args=[self.object.artist.pk])


def album_remove(request, pk):
    album = get_object_or_404(Post, pk=pk)
    album.delete()
    return redirect('artist_detail')


"""
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
"""
