from django.contrib import admin
from .models import Artist, Artwork, ArtworkImage, Workshop, WorkshopMember


class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1


class WorkshopMemberInline(admin.TabularInline):
    model = WorkshopMember
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'medium', 'order']
    search_fields = ['name', 'city']
    list_editable = ['order']


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'year', 'medium']
    search_fields = ['title', 'artist__name']
    list_filter = ['artist']
    inlines = [ArtworkImageInline]


@admin.register(ArtworkImage)
class ArtworkImageAdmin(admin.ModelAdmin):
    list_display = ['artwork', 'order']


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    inlines = [WorkshopMemberInline]