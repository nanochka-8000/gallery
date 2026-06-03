from django.db import models


class ShopProduct(models.Model):
    CATEGORY_CHOICES = [
        ('artwork', 'Работа'),
        ('print', 'Принт'),
        ('book', 'Книга / Каталог'),
        ('merchandise', 'Сувенир'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='shop/', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='KGS')
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='artwork')
    artist_name = models.CharField(max_length=200, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Товар'
        verbose_name_plural = 'Магазин'
