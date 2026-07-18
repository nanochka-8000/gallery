from django.shortcuts import render
from exhibitions.models import Exhibition

def home(request):
    featured_exhibition = Exhibition.objects.filter(status='current').first()
    return render(request, 'home.html', {
        'featured_exhibition': featured_exhibition,
    })

def about(request):
    return render(request, 'about.html')

def home(request):
    featured_exhibition = Exhibition.objects.filter(status='current').prefetch_related('images').first()
    return render(request, 'home.html', {
        'featured_exhibition': featured_exhibition,
    })


def about(request):
    return render(request, 'about.html')