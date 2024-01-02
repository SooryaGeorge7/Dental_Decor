from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Order


class CheckoutViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_cache_checkout_data_view(self):
        response = self.client.post(reverse('cache_checkout_data'))
        self.assertEqual(response.status_code, 400)

    def test_checkout_view_unauthenticated_user(self):
        response = self.client.get(reverse('shop_checkout'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_view_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(reverse('shop_checkout'))
        self.assertEqual(response.status_code, 302)

    def test_checkout_success_view(self):
        order = Order.objects.create(
            full_name='Test User',
            email='test@example.com',
            phone_number='1234567890',
            country='US',
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Test St',
            street_address2='Apt 4',
            county='Test County',
        )

        response = self.client.get(reverse('checkout_success', args=[order.order_number]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')