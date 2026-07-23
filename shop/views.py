from django.shortcuts import render, get_object_or_404
# Импортируем модель Artwork из приложения artists, так как товары хранятся именно там
from artists.models import Artwork


def shop_list(request):
    # Получаем все работы, у которых стоит галочка "Показывать на сайте"
    # Судя по твоим миграциям, поле называется is_published. Если это не так, замени на актуальное.
    artworks = Artwork.objects.filter(is_published=True)

    # Передаем в шаблон переменную artworks, как мы и прописали в HTML
    return render(request, 'shop/shop_list.html', {
        'artworks': artworks,
    })


def shop_detail(request, pk):
    # Обновляем детальную страницу, чтобы она тоже искала по модели Artwork
    artwork = get_object_or_404(Artwork, pk=pk, is_published=True)
    return render(request, 'shop/shop_detail.html', {'artwork': artwork})