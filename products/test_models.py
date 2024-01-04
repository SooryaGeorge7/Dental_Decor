from django.test import TestCase
from .models import Category, Product

class CategoryModelTest(TestCase):

    def test_category_model_creation(self):
        category = Category.objects.create(
            name='Dentaldecor Category',
            notes='This is a Dentaldecor category.',
            friendly_name='Dentaldecor Friendly Name'
        )
        self.assertIsInstance(category, Category)
        self.assertEqual(category.name, 'Dentaldecor Category')
        self.assertEqual(category.notes, 'This is a Dentaldecor category.')
        self.assertEqual(category.friendly_name, 'Dentaldecor Friendly Name')

    def test_category_model_str_method(self):
        category = Category.objects.create(name='Dentaldecor Category')
        self.assertEqual(str(category), 'Dentaldecor Category')

    def test_category_model_get_friendly_name_method(self):
        category = Category.objects.create(name='Dentaldecor Category', friendly_name='Dentaldecor Friendly Name')
        self.assertEqual(category.get_friendly_name(), 'Dentaldecor Friendly Name')

class ProductModelTest(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='Dentaldecor Category')

    def test_product_model_creation(self):
        product = Product.objects.create(
            category=self.category,
            name='Dentaldecor Product',
            description='This is a Dentaldecor product.',
            has_sizes=True,
            price=10.00,
            image_url='https://example.com/image.jpg',
        )
        self.assertIsInstance(product, Product)
        self.assertEqual(product.category, self.category)
        self.assertIsNotNone(product.sku)
        self.assertEqual(product.name, 'Dentaldecor Product')
        self.assertEqual(product.description, 'This is a Dentaldecor product.')
        self.assertTrue(product.has_sizes)
        self.assertEqual(product.price, 10.00)
        self.assertEqual(product.image_url, 'https://example.com/image.jpg')

