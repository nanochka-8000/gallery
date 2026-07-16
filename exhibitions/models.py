from django.db import models
from artists.models import Artist, Artwork, Workshop

class Exhibition(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Предстоящая'),
        ('current', 'Текущая'),
        ('past', 'Прошедшая'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='exhibitions/', blank=True)
    artists = models.ManyToManyField(Artist, blank=True)
    workshops = models.ManyToManyField(Workshop, blank=True)
    artworks = models.ManyToManyField(Artwork, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    location = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-start_date']