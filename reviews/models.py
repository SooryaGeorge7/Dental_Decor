from django.db import models

from django.contrib.auth.models import User
from products.models import Product
from django.core.validators import MaxLengthValidator


# Create your models here.
class Review(models.Model):
    """
    Model for creating a User Review
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(
        auto_now_add=True,
        null=True,
    )
    Rating = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )

    product_rating = models.IntegerField(choices=Rating, default=0)
    
    comment_text = models.TextField(
        null=True,
        blank=True,
        validators=[MaxLengthValidator(500)],
    )

    class Meta:
        """
        Order by when review was created on
        """
        ordering = ["-created_on"]

    def __str__(self):
        """
        Returns the username and the Product name as a string
        representation of the object.
        """
        return f"{self.user.username}'s review of {self.product.name}"