from django.contrib import admin
from .models import Artist, Artwork, ArtworkImage, Workshop, WorkshopMember


class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1


class WorkshopMemberInline(admin.TabularInline):
    model = WorkshopMember
    extra = 1
    fields = ['name', 'role', 'artist', 'quote', 'bio', 'photo']


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'medium', 'order']
    search_fields = ['name', 'city']
    list_editable = ['order']


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'year', 'medium', 'status']
    search_fields = ['title', 'artist__name']
    list_filter = ['artist', 'status']
    inlines = [ArtworkImageInline]
    filter_horizontal = ['designed_by', 'made_by', 'designed_by_workshops', 'made_by_workshops']


@admin.register(ArtworkImage)
class ArtworkImageAdmin(admin.ModelAdmin):
    list_display = ['artwork', 'order']


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['name', 'city']
    inlines = [WorkshopMemberInline]