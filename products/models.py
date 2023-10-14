from django.db import models
from django.utils.crypto import get_random_string


class Category(models.Model):
    name = models.CharField(max_length=254)
    notes = models.TextField()
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

def unique_sku():
    sku = get_random_string(length=7)
    while Product.objects.filter(sku=sku).exists():
        sku = get_random_string(length=7)
    return sku


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.SlugField( unique=True, default=unique_sku)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name