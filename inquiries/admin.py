from django.contrib import admin
from .models import Inquiry

@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'artwork', 'created_at']
    readonly_fields = ['name', 'email', 'message', 'artwork', 'created_at']