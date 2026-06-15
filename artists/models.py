from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)  # имя художника
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
    dimensions = models.CharField(max_length=100, blank=True)  # размер
    description = models.TextField(blank=True)  # описание
    image = models.ImageField(upload_to='artworks/')  # фото работы
    price = models.CharField(max_length=100, blank=True)  # цена (опционально)

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