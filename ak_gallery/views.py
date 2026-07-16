from django.shortcuts import render
from artists.models import Artist
from exhibitions.models import Exhibition

def home(request):
    featured_exhibition = Exhibition.objects.filter(status='current').first()
    return render(request, 'home.html', {
        'featured_exhibition': featured_exhibition,
    })

def about(request):
    return render(request, 'about.html')