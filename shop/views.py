from django.shortcuts import render, get_object_or_404
from artists.models import Artwork


def shop_list(request):
    # Только опубликованные И не проданные
    artworks = Artwork.objects.filter(is_published=True, is_sold=False)
    return render(request, 'shop/shop_list.html', {
        'artworks': artworks,
    })


def shop_detail(request, pk):
    # На детальную страницу магазина проданные не пускаем
    artwork = get_object_or_404(Artwork, pk=pk, is_published=True)
    return render(request, 'shop/shop_detail.html', {'artwork': artwork})