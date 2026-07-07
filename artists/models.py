from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    bio = models.TextField(blank=True)
    quote = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='artists/')
    city = models.CharField(max_length=100, blank=True)
    medium = models.CharField(max_length=200, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return self.name


class Workshop(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    photo = models.ImageField(upload_to='workshops/', blank=True)
    city = models.CharField(max_length=100, blank=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True)

    def __str__(self):
        return self.name


class WorkshopMember(models.Model):
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE, related_name='members')
    is_published = models.BooleanField(default=True, verbose_name='Показывать на сайте')
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    quote = models.CharField(max_length=300, blank=True)
    photo = models.ImageField(upload_to='workshop_members/', blank=True)

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