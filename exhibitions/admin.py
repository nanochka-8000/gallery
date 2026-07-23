from django.contrib import admin
from .models import Exhibition, ExhibitionImage


class ExhibitionImageInline(admin.TabularInline):
    model = ExhibitionImage
    extra = 3
    fields = ['image', 'caption', 'order']


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'start_date', 'end_date']
    list_filter = ['status']
    search_fields = ['title']
    filter_horizontal = ('artists', 'workshops')
    inlines = [ExhibitionImageInline]