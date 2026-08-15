from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Artist, Artwork, Workshop, WorkshopMember, Series


def artist_list(request):
    artists = Artist.objects.filter(is_published=True).order_by('order')
    workshops = Workshop.objects.filter(is_published=True)
    return render(request, 'artists/artist_list.html', {
        'artists': artists,
        'workshops': workshops,
    })


def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)

    all_artworks = Artwork.objects.filter(
        Q(designed_by=artist) | Q(made_by=artist),
        is_published=True,
    ).distinct()

    # серии: либо напрямую привязаны к мастеру, либо содержат его работы
    series = Series.objects.filter(
        Q(artists=artist) | Q(artworks__in=all_artworks),
        is_published=True,
    ).distinct()

    standalone_artworks = all_artworks.filter(series__isnull=True)

    return render(request, 'artists/artist_detail.html', {
        'artist': artist,
        'series': series,
        'standalone_artworks': standalone_artworks,
    })


def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk, is_published=True)
    return render(request, 'artists/artwork_detail.html', {'artwork': artwork})


def workshop_detail(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    members = workshop.members.filter(is_published=True)

    all_artworks = Artwork.objects.filter(
        Q(designed_by_workshops=workshop) | Q(made_by_workshops=workshop),
        is_published=True,
    ).distinct()

    series = Series.objects.filter(
        Q(workshops=workshop) | Q(artworks__in=all_artworks),
        is_published=True,
    ).distinct()

    standalone_artworks = all_artworks.filter(series__isnull=True)

    return render(request, 'artists/workshop_detail.html', {
        'workshop': workshop,
        'members': members,
        'series': series,
        'standalone_artworks': standalone_artworks,
    })


def workshop_member_detail(request, pk):
    member = get_object_or_404(WorkshopMember, pk=pk)
    return render(request, 'artists/workshop_member_detail.html', {'member': member})


def series_detail(request, pk):
    series = get_object_or_404(Series, pk=pk)
    artworks = series.artworks.filter(is_published=True)
    return render(request, 'artists/series_detail.html', {
        'series': series,
        'artworks': artworks,
    })