from django.contrib import admin
from .models import Artist, Artwork, ArtworkImage, Workshop, WorkshopMember, Series


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
    list_display = ['title', 'get_authors', 'year', 'medium', 'status']
    search_fields = ['title', 'designed_by__name', 'made_by__name']
    list_filter = ['status', 'designed_by', 'made_by']
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
    list_display = ['name', 'city']
    inlines = [WorkshopMemberInline]

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'year']
    search_fields = ['title']