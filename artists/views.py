from django.shortcuts import render, get_object_or_404
from .models import Artist, Artwork, Workshop

def artist_list(request):
    artists = Artist.objects.all()
    workshops = Workshop.objects.all()
    return render(request, 'artists/artist_list.html', {'artists': artists, 'workshops': workshops})

def artist_detail(request, pk):
    artist = get_object_or_404(Artist, pk=pk)
    # работы где художник — основной автор
    own_artworks = artist.artworks.all()
    # работы где художник — дизайнер
    designed = artist.designed_artworks.all()
    # работы где художник — изготовитель
    made = artist.made_artworks.all()
    # объединяем все без повторений
    all_ids = set(list(own_artworks.values_list('id', flat=True)) +
                  list(designed.values_list('id', flat=True)) +
                  list(made.values_list('id', flat=True)))
    artworks = Artwork.objects.filter(id__in=all_ids)
    return render(request, 'artists/artist_detail.html', {'artist': artist, 'artworks': artworks})

def artwork_detail(request, pk):
    artwork = get_object_or_404(Artwork, pk=pk)
    return render(request, 'artists/artwork_detail.html', {'artwork': artwork})

def workshop_detail(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    members = workshop.members.all()
    # работы где мастерская — дизайнер или изготовитель
    designed = workshop.designed_artworks.all()
    made = workshop.made_artworks.all()
    all_ids = set(list(designed.values_list('id', flat=True)) +
                  list(made.values_list('id', flat=True)))
    artworks = Artwork.objects.filter(id__in=all_ids)
    return render(request, 'artists/workshop_detail.html', {'workshop': workshop, 'members': members, 'artworks': artworks})