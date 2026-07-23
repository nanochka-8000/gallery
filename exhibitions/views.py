from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Exhibition


def exhibition_list(request):
    today = timezone.now().date()

    # Текущие: дата начала <= сегодня И дата окончания >= сегодня
    current = Exhibition.objects.filter(start_date__lte=today, end_date__gte=today).order_by('start_date')

    # Предстоящие: дата начала > сегодня
    upcoming = Exhibition.objects.filter(start_date__gt=today).order_by('start_date')

    # Прошедшие (архив): дата окончания < сегодня
    past = Exhibition.objects.filter(end_date__lt=today).order_by('-end_date')

    return render(request, 'exhibitions/exhibition_list.html', {
        'current': current,
        'upcoming': upcoming,
        'past': past,
    })


def exhibition_detail(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    # Получаем все дополнительные фото выставки для карусели
    images = exhibition.images.all()

    return render(request, 'exhibitions/exhibition_details.html', {
        'exhibition': exhibition,
        'images': images,
    })


def exhibition_artworks(request, pk):
    exhibition = get_object_or_404(Exhibition, pk=pk)
    # Используем правильное имя связи, которое мы задали в models.py
    artworks = exhibition.exhibition_artworks.all()

    return render(request, 'exhibitions/exhibition_artworks.html', {
        'exhibition': exhibition,
        'artworks': artworks,
    })