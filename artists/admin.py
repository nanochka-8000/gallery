from django.contrib import admin
from .models import Artist, Artwork, ArtworkImage, Workshop, WorkshopMember, Series


class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1


class WorkshopMemberInline(admin.TabularInline):
    model = WorkshopMember
    extra = 1


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'medium', 'order', 'is_published']
    list_editable = ['order', 'is_published']
    search_fields = ['name', 'city']


@admin.register(Artwork)
class ArtworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_authors', 'series', 'year', 'medium', 'is_published']
    list_editable = ['is_published']
    list_filter = ['series', 'is_published', 'designed_by', 'made_by']
    search_fields = ['title', 'designed_by__name', 'made_by__name']
    inlines = [ArtworkImageInline]
    filter_horizontal = ['designed_by', 'made_by', 'designed_by_workshops', 'made_by_workshops']

    def get_authors(self, obj):
        designers = list(obj.designed_by.values_list('name', flat=True))
        makers = list(obj.made_by.values_list('name', flat=True))
        all_authors = designers + [m for m in makers if m not in designers]
        return ", ".join(all_authors) or "—"
    get_authors.short_description = 'Авторы'


@admin.register(ArtworkImage)
class ArtworkImageAdmin(admin.ModelAdmin):
    list_display = ['artwork', 'order']


@admin.register(Workshop)
class WorkshopAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'is_published']
    list_editable = ['is_published']
    inlines = [WorkshopMemberInline]

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_published']
    list_editable = ['order', 'is_published']
    search_fields = ['title']
    filter_horizontal = ['artists', 'workshops']