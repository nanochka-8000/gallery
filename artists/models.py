from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)  # имя художника
    bio = models.TextField(blank=True)  # биография
    photo = models.ImageField(upload_to='artists/')  # фото художника
    city = models.CharField(max_length=100, blank=True)  # город
    medium = models.CharField(max_length=200, blank=True)  # техника (живопись, войлок...)

    def __str__(self):
        return self.name


class Artwork(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artworks')
    title = models.CharField(max_length=200)  # название работы
    year = models.IntegerField(blank=True, null=True)  # год
    medium = models.CharField(max_length=200, blank=True)  # материал
    dimensions = models.CharField(max_length=100, blank=True)  # размер
    description = models.TextField(blank=True)  # описание
    image = models.ImageField(upload_to='artworks/')  # фото работы
    price = models.CharField(max_length=100, blank=True)  # цена (опционально)

    def __str__(self):
        return f"{self.title} — {self.artist.name}"