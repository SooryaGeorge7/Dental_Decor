from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from .models import Review

class ReviewModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product', description='Test Description', price=10.00
        )

    def test_review_model_fields(self):
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            product_rating=4,
            comment_text='Test comment',
        )
        self.assertEqual(review.user, self.user)
        self.assertEqual(review.product, self.product)
        self.assertEqual(review.product_rating, 4)
        self.assertEqual(review.comment_text, 'Test comment')

    def test_review_model_default_values(self):
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            product_rating=0,
            comment_text=None,
        )
        self.assertEqual(review.product_rating, 0)
        self.assertIsNone(review.comment_text)

    def test_review_model_ordering(self):
        review1 = Review.objects.create(
            user=self.user,
            product=self.product,
            product_rating=4,
            comment_text='Test comment 1',
        )
        review2 = Review.objects.create(
            user=self.user,
            product=self.product,
            product_rating=5,
            comment_text='Test comment 2',
        )
        reviews = Review.objects.all()
        self.assertEqual(reviews[0], review2)
        self.assertEqual(reviews[1], review1)

    def test_review_model_str_method(self):
        review = Review.objects.create(
            user=self.user,
            product=self.product,
            product_rating=4,
            comment_text='Test comment',
        )
        expected_str = f"{self.user.username}'s review of {self.product.name}"
        self.assertEqual(str(review), expected_str)

