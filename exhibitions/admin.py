from django.contrib import admin
from .models import Exhibition

@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'start_date', 'end_date']
    list_filter = ['status']
    search_fields = ['title']