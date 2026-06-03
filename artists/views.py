from django.shortcuts import render, get_object_or_404
from .models import Artist, Artwork

def artist_list(request):
    artists = Artist.objects.all()
    return render(request, 'artists/artist_list.html', {'artists': artists})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artworks = artist.artworks.all()
    return render(request, 'artists/artist_detail.html', {'artist': artist, 'artworks': artworks})

def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artists/artwork_detail.html', {'artwork': artwork})