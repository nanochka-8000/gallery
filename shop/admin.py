from django.contrib import admin
from .models import ShopProduct


@admin.register(ShopProduct)
class ShopProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist_name', 'category', 'price', 'currency', 'is_available')
    list_filter = ('category', 'is_available')
    list_editable = ('is_available', 'price')
    search_fields = ('title', 'artist_name')
