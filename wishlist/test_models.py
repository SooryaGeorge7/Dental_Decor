from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from wishlist.models import Wishlist


class WishlistModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product', description='Test Description', price=10.00
        )

    def test_wishlist_creation(self):
        """
        Test case for creating a wishlist item.
        """
        wishlist_item = Wishlist.objects.create(user=self.user, product=self.product)

        self.assertTrue(isinstance(wishlist_item, Wishlist))
        self.assertEqual(wishlist_item.user, self.user)
        self.assertEqual(wishlist_item.product, self.product)
