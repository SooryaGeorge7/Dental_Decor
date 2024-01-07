from django.test import TestCase
from .forms import UserProfileForm
from django.contrib.auth.models import User


class UserProfileFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
    def test_user_profile_form_creation(self):
        """
        Test case to ensure that the UserProfileForm is created successfully.
        """
        form = UserProfileForm()
        self.assertIsInstance(form, UserProfileForm)

    def test_user_profile_form_labels(self):
        """
        Test case to check if the labels of the UserProfileForm fields match the expected labels.
        """

        form = UserProfileForm()
        expected_labels = {
            'default_phone_number': 'Phone Number',
            'default_postcode': 'Postal Code',
            'default_town_or_city': 'Town or City',
            'default_street_address1': 'Street Address 1',
            'default_street_address2': 'Street Address 2',
            'default_county': 'County, State or Locality',
            'default_country': 'Country',
        }
        for field, expected_label in expected_labels.items():
            self.assertEqual(form.fields[field].label, expected_label)

    def test_user_profile_form_widget_attributes(self):
        """
        Test case to check if the widget attributes of UserProfileForm fields match the expected values.
        """
        form = UserProfileForm()
        self.assertTrue(form.fields['default_phone_number'].widget.attrs.get('autofocus'))
        expected_classes = 'border-black rounded-0 profile-form-input'
        for field in form.fields:
            self.assertEqual(form.fields[field].widget.attrs['class'], expected_classes)

    def test_user_profile_form_exclude_user_field(self):
        """
        Test case to ensure that the 'user' field is excluded from the UserProfileForm.
        """
        form = UserProfileForm()
        self.assertNotIn('user', form.fields)

