from django.contrib import admin
from .models import Artist, Artwork

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'medium']
    search_fields = ['name', 'city']

@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'year', 'medium']
    search_fields = ['title', 'artist__name']
    list_filter = ['artist']