from django.contrib import admin


from .models import Artist, Artwork, ArtworkImage, Workshop, WorkshopMember, Series, Tag


class ArtworkImageInline(admin.TabularInline):
    model = ArtworkImage
    extra = 1


class WorkshopMemberInline(admin.TabularInline):
    model = WorkshopMember
    extra = 1

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'medium', 'order', 'is_published']
    list_editable = ['order', 'is_published']
    search_fields = ['name', 'city']


@admin.register(Artwork) #[cite: 6]
class ArtworkAdmin(admin.ModelAdmin): #[cite: 6]
    list_display = ['title', 'exhibition', 'code', 'price', 'is_sold', 'is_published'] #[cite: 6]
    list_editable = ['is_sold', 'is_published'] #[cite: 6]
    list_filter = ['exhibition', 'is_sold', 'is_published', 'series', 'tags']
    search_fields = ['title', 'code', 'description', 'price', 'designed_by__name', 'made_by__name'] #[cite: 6]
    inlines = [ArtworkImageInline] #[cite: 6]
    filter_horizontal = ['designed_by', 'made_by', 'designed_by_workshops', 'made_by_workshops', 'tags']



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