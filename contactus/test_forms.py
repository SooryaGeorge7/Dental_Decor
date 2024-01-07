from django.test import TestCase
from .forms import ContactForm

class ContactFormTest(TestCase):

    def test_valid_contact_form(self):
        """
        Test case for a valid contact form.
        """
        data = {
            'name': 'Soorya George',
            'email': 'soorya@example.com',
            'phone': '1237777890',
            'message': 'Hello.'
        }
        form = ContactForm(data)
        self.assertTrue(form.is_valid())

    def test_invalid_contact_form_missing_required_fields(self):
        """
        Test case for an invalid contact form with missing required fields.
        """
        data = {
            'name': '',
            'email': '',
            'phone': '',
            'message': ''
        }
        form = ContactForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['This field is required.'])
        self.assertEqual(form.errors['email'], ['This field is required.'])
        self.assertEqual(form.errors['phone'], ['This field is required.'])
        self.assertEqual(form.errors['message'], ['This field is required.'])

    def test_invalid_contact_form_invalid_email(self):
        """
        Test case for an invalid contact form with an invalid email address.
        """
        data = {
            'name': 'Soorya George',
            'email': 'invalid-email',
            'phone': '1237777890',
            'message': 'Hello.'
        }
        form = ContactForm(data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

    def test_form_widgets(self):
        """
        Test case for contact form widget attributes.
        """
        form = ContactForm()
        self.assertEqual(form.fields['message'].widget.attrs['rows'], 5)

    def test_form_labels(self):
        """
        Test case for contact form field labels.
        """
        form = ContactForm()
        self.assertEqual(form.fields['name'].label, 'Name')
        self.assertEqual(form.fields['email'].label, 'Email')
        self.assertEqual(form.fields['phone'].label, 'Phone')
        self.assertEqual(form.fields['message'].label, 'Message')
