from django.test import TestCase
from django.urls import reverse


class ShoppingBagPageTests(TestCase):
    def test_cart_page(self):
        response = self.client.get(reverse('view_shoppingbag'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoppingbag/shoppingbag.html')
        self.assertContains(
            response, '<h1 class="logo-font">Shopping Bag</h1>')
        self.assertNotContains(response, 'Not on the page')