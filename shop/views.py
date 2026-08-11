from django.shortcuts import render, get_object_or_404  # [cite: 7]
from artists.models import Artwork, Tag  # Добавили импорт Tag


def shop_list(request):
    artworks = Artwork.objects.filter(is_published=True, is_sold=False)
    tags = Tag.objects.all()

    selected_tag = request.GET.get('tag')
    if selected_tag:
        artworks = artworks.filter(tags__slug=selected_tag)

    return render(request, 'shop/shop_list.html', {
        'artworks': artworks,
        'tags': tags,
        'selected_tag': selected_tag,
    })


def shop_detail(request, pk):  # [cite: 7]
    artwork = get_object_or_404(Artwork, pk=pk, is_published=True)
    return render(request, 'shop/shop_detail.html', {'artwork': artwork})