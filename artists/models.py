from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)  # имя художника
    order = models.IntegerField(default=0)
    bio = models.TextField(blank=True)  # биография
    quote = models.CharField(max_length=300, blank=True)  # цитата художника
    photo = models.ImageField(upload_to='artists/')  # фото художника
    city = models.CharField(max_length=100, blank=True)  # город
    medium = models.CharField(max_length=200, blank=True)  # техника (живопись, войлок...)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)  # QR код

    def __str__(self):
        return self.name


class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    title = models.CharField(max_length=200)  # название работы
    year = models.IntegerField(blank=True, null=True)  # год
    medium = models.CharField(max_length=200, blank=True)  # материал
    weight = models.CharField(max_length=100, blank=True)  # вес работы
    dimensions = models.CharField(max_length=100, blank=True)  # размер
    description = models.TextField(blank=True)  # описание
    image = models.ImageField(upload_to='artworks/')  # фото работы
    price = models.CharField(max_length=100, blank=True)  # цена (опционально)
    designed_by = models.ManyToManyField(Artist, blank=True, related_name='designed_artworks')
    made_by = models.ManyToManyField(Artist, blank=True, related_name='made_artworks')
    designed_by_workshops = models.ManyToManyField('Workshop', blank=True, related_name='designed_artworks')
    made_by_workshops = models.ManyToManyField('Workshop', blank=True, related_name='made_artworks')

    def __str__(self):
        return f"{self.title} — {self.artist.name}"
    
class Workshop(models.Model):
    name = models.CharField(max_length=200)  # название мастерской
    subtitle = models.CharField(max_length=200, blank=True)  # вторая строка названия
    bio = models.TextField(blank=True)  # общее описание
    photo = models.ImageField(upload_to='workshops/', blank=True)  # фото мастерской
    city = models.CharField(max_length=100, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)  # QR код

    def __str__(self):
        return self.name

class WorkshopMember(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=200)  # имя члена семьи
    bio = models.TextField(blank=True)  # bio члена семьи
    quote = models.CharField(max_length=300, blank=True)  # цитата
    photo = models.ImageField(upload_to='workshop_members/', blank=True)
    
    def __str__(self):
        return f"{self.name} — {self.workshop.name}"
    
class ArtworkImage(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='artworks/gallery/')
    order = models.IntegerField(default=0)  # порядок фото
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"Фото {self.order} — {self.artwork.title}"