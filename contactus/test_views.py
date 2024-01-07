from django.test import TestCase
from django.urls import reverse
from django.core import mail
from .forms import ContactForm

class ContactUsViewTest(TestCase):
    def test_contact_us_view_post_valid_form(self):
        """
        Test case for submitting a valid contact form through the Contact Us view.
        """
        data = {
            'name': 'Soorya george',
            'email': 'soorya@example.com',
            'message': 'Hello',
        }

        response = self.client.post(reverse('contact_us'), data)
        self.assertEqual(response.status_code, 302) 


    def test_contact_us_view_post_invalid_form(self):
        """
        Test case for submitting an invalid contact form through the Contact Us view.
        """
        data = {
            'name': 'Soorya George',
            'email': 'invalid_email', 
            'message': 'Hello',
        }

        response = self.client.post(reverse('contact_us'), data)
        self.assertEqual(response.status_code, 302)  

        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'There is an error found in the form')
