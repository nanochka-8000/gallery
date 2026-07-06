from django.shortcuts import render, get_object_or_404
from .models import Artist, Artwork, Workshop, Series


def artist_list(request):
    artists = Artist.objects.all().order_by('order')
    workshops = Workshop.objects.all()
    return render(request, 'artists/artist_list.html', {'artists': artists, 'workshops': workshops})


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    artworks = (artist.designed_artworks.all() | artist.made_artworks.all()).distinct()
    # серии этого художника
    series_ids = artworks.exclude(series=None).values_list('series_id', flat=True).distinct()
    series_list = Series.objects.filter(id__in=series_ids)
    # работы без серии
    solo_artworks = artworks.filter(series=None)
    return render(request, 'artists/artist_detail.html', {
        'artist': artist,
        'artworks': solo_artworks,
        'series_list': series_list,
    })


def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artists/artwork_detail.html', {'artwork': artwork})


def series_detail(request, pk):
    series = get_object_or_404(Series, pk=pk)
    artworks = series.artworks.all()
    return render(request, 'artists/series_detail.html', {'series': series, 'artworks': artworks})


def workshop_detail(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    members = workshop.members.all()
    artworks = (workshop.designed_artworks.all() | workshop.made_artworks.all()).distinct()
    return render(request, 'artists/workshop_detail.html', {
        'workshop': workshop,
        'members': members,
        'artworks': artworks,
    })