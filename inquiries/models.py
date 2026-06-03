from django.db import models
from artists.models import Artwork

class Inquiry(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='inquiries')
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.artwork.title}"

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Inquiries'