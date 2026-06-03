from django.shortcuts import render, redirect, get_object_or_404
from artists.models import Artwork
from .models import Inquiry

def inquiry(request, artwork_pk):
    artwork = get_object_or_404(Artwork, pk=artwork_pk)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Inquiry.objects.create(
            artwork=artwork,
            name=name,
            email=email,
            message=message
        )
        return redirect(f'/artists/artwork/{artwork_pk}/?sent=true')
    return render(request, 'inquiries/inquiry.html', {'artwork': artwork})