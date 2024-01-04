from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from checkout.models import Order

class ProfileViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.customer_profile = UserProfile.objects.update(
            default_phone_number='67373',
            default_country='IE',
        )
    def test_profile_view_get(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)

    def test_profile_view_post_valid_form(self):
        response = self.client.post(reverse('profile'), data={'your_form_data': 'here'})
        self.assertEqual(response.status_code, 302)  
        response = self.client.get(response.url)
        self.assertEqual(response.status_code, 200)  

    