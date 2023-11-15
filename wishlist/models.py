
# Create your models here.
from django.db import models
from django.contrib.auth.models import User

# Internal:
from products.models import Product
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class Wishlist(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return f'{self.product.name} in {self.product.category}'

