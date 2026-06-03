from django.shortcuts import render
from artists.models import Artist
from exhibitions.models import Exhibition

def home(request):
    current_exhibitions = Exhibition.objects.filter(status='current')
    upcoming_exhibitions = Exhibition.objects.filter(status='upcoming')
    artists = Artist.objects.all()[:6]
    return render(request, 'home.html', {
        'current_exhibitions': current_exhibitions,
        'upcoming_exhibitions': upcoming_exhibitions,
        'artists': artists,
    })

def about(request):
    return render(request, 'about.html')