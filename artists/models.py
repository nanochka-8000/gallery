from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
<<<<<<< HEAD
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

    STATUS_CHOICES = [
        ('available', 'В наличии'),
        ('sold', 'Продано'),
        ('reserved', 'Зарезервировано'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return f"{self.title} — {self.artist.name}"
    
class Workshop(models.Model):
    name = models.CharField(max_length=200)  # название мастерской
    subtitle = models.CharField(max_length=200, blank=True)  # вторая строка названия
    bio = models.TextField(blank=True)  # общее описание
    photo = models.ImageField(upload_to='workshops/', blank=True)  # фото мастерской
=======
    bio = models.TextField(blank=True)
    quote = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='artists/')
>>>>>>> e43b2ddf9de039fabe7de76b494e3d41df4ef3a3
    city = models.CharField(max_length=100, blank=True)
    medium = models.CharField(max_length=200, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return self.name


class Workshop(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='workshops/', blank=True)
    city = models.CharField(max_length=100, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return self.name


class WorkshopMember(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    quote = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='workshop_members/', blank=True)
<<<<<<< HEAD
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True, blank=True,
                               related_name='workshop_memberships')
    role = models.CharField(max_length=100, blank=True)  # Куратор, Мастер и т.д.
    
=======

>>>>>>> e43b2ddf9de039fabe7de76b494e3d41df4ef3a3
    def __str__(self):
        return f"{self.name} — {self.workshop.name}"


class Artwork(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    medium = models.CharField(max_length=200, blank=True)
    weight = models.CharField(max_length=100, blank=True)
    dimensions = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='artworks/')
    price = models.CharField(max_length=100, blank=True)

    designed_by = models.ManyToManyField(Artist, blank=True, related_name='designed_artworks')
    made_by = models.ManyToManyField(Artist, blank=True, related_name='made_artworks')
    designed_by_workshops = models.ManyToManyField(Workshop, blank=True, related_name='designed_artworks')
    made_by_workshops = models.ManyToManyField(Workshop, blank=True, related_name='made_artworks')

    def __str__(self):
        # собираем всех авторов для читаемого отображения в админке
        designers = list(self.designed_by.values_list('name', flat=True))
        makers = list(self.made_by.values_list('name', flat=True))
        all_authors = designers + [m for m in makers if m not in designers]
        authors_str = ", ".join(all_authors) if all_authors else "без автора"
        return f"{self.title} — {authors_str}"


class ArtworkImage(models.Model):
    artwork = models.ForeignKey(Artwork, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='artworks/gallery/')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Фото {self.order} — {self.artwork.title}"