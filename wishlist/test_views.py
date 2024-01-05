from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client
from products.models import Product
from wishlist.models import Wishlist

class WishlistViewsTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product', description='Test Description', price=10.00
        )
        self.client = Client()

    def test_wishlist_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('wishlist'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'wishlist/wishlist.html')

    def test_add_to_wishlist_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('add_to_wishlist', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Wishlist.objects.count(), 1)
        self.assertEqual(Wishlist.objects.first().product, self.product)

    def test_remove_from_wishlist_view(self):
        wishlist_item = Wishlist.objects.create(user=self.user, product=self.product)
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('remove_from_wishlist', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)  
        self.assertEqual(Wishlist.objects.count(), 0)
