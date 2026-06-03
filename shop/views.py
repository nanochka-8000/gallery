from django.shortcuts import render, get_object_or_404
from .models import ShopProduct


def shop_list(request):
    category = request.GET.get('category', '')
    products = ShopProduct.objects.filter(is_available=True)
    if category:
        products = products.filter(category=category)
    categories = ShopProduct.CATEGORY_CHOICES
    return render(request, 'shop/shop_list.html', {
        'products': products,
        'categories': categories,
        'active_category': category,
    })


def shop_detail(request, pk):
    product = get_object_or_404(ShopProduct, pk=pk, is_available=True)
    return render(request, 'shop/shop_detail.html', {'product': product})
