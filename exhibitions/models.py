from django.db import models
from artists.models import Artist, Artwork, Workshop
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFit

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

class ExhibitionImage(models.Model):
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='exhibitions/gallery/')
    image_thumb = ImageSpecField(
        source='image',
        processors=[ResizeToFit(1400, 1050)],
        format='JPEG',
        options={'quality': 85}
    )
    caption = models.CharField(max_length=200, blank=True, verbose_name='Подпись (необязательно)')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Фото с выставки'
        verbose_name_plural = 'Фото с выставки'

    def __str__(self):
        return f"Фото {self.order} — {self.exhibition.title}"