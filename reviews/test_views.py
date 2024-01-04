from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product
from .models import Review
from .forms import RatingForm

class ReviewsViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        self.product = Product.objects.create(
            name='Test Product', description='Test Description', price=10.00
        )
        self.review = Review.objects.create(
            user=self.user,
            product=self.product,
            product_rating=4,
            comment_text='Test comment',
        )

    def test_add_review_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_review', args=[self.product.id]), data={'product_rating': 5})
        self.assertEqual(response.status_code, 302) 

    def test_add_review_view_authenticated_user_duplicate_review(self):
        Review.objects.create(
            user=self.user,
            product=self.product,
            product_rating=4,
            comment_text='Another test comment',
        )
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('add_review', args=[self.product.id]), data={'product_rating': 3})
        self.assertEqual(response.status_code, 302) 

    def test_edit_review_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('edit_review', args=[self.review.id]), data={'product_rating': 3})
        self.assertEqual(response.status_code, 302)  
        self.review.refresh_from_db()
        self.assertEqual(self.review.product_rating, 3) 

    def test_delete_review_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.post(reverse('delete_review', args=[self.review.id]))
        self.assertEqual(response.status_code, 302) 

    def test_add_review_view_unauthenticated_user(self):
        response = self.client.post(reverse('add_review', args=[self.product.id]), data={'product_rating': 5})
        self.assertEqual(response.status_code, 302)  

    def test_edit_review_view_unauthenticated_user(self):
        response = self.client.post(reverse('edit_review', args=[self.review.id]), data={'product_rating': 3})
        self.assertEqual(response.status_code, 302)  

    def test_delete_review_view_unauthenticated_user(self):
        response = self.client.post(reverse('delete_review', args=[self.review.id]))
        self.assertEqual(response.status_code, 302)  

