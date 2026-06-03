from django.shortcuts import render, get_object_or_404
from .models import Exhibition

def exhibition_list(request):
    current = Exhibition.objects.filter(status='current')
    upcoming = Exhibition.objects.filter(status='upcoming')
    past = Exhibition.objects.filter(status='past')
    return render(request, 'exhibitions/exhibition_list.html', {
        'current': current,
        'upcoming': upcoming,
        'past': past,
    })

def exhibition_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    return render(request, 'exhibitions/exhibition_details.html', {
        'exhibition': exhibition,
    })
