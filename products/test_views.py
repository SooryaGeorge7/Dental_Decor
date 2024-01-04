from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Product, Category
from reviews.models import Review


class ProductViewsTest(TestCase):

    def setUp(self):
        # Create a superuser for testing
        self.user = User.objects.create_superuser(
            username='admin', password='admin', email='admin@example.com'
        )

        # Create some categories for testing
        self.category1 = Category.objects.create(name='Category 1')
        self.category2 = Category.objects.create(name='Category 2')

        # Create some products for testing
        self.product1 = Product.objects.create(
            name='Product 1', description='Description 1',
            price=10.00, category=self.category1
        )
        self.product2 = Product.objects.create(
            name='Product 2', description='Description 2',
            price=20.00, category=self.category2
        )

    def test_shop_products_view(self):
        url = reverse('shop_products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/shop_products.html')

    def test_product_detail_view(self):
        url = reverse('product_detail', args=[self.product1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    