from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .models import UserProfile


class TestCustomerProfile(TestCase):
    """
    Test cases for the CustomerProfile model.
    """
    @classmethod
    def setUp(self):
        """
        creating and saving a new test user
        """
        self.user = User.objects.create(
            username='TestName',
            password='12377',
            email='test@username.com',
            id='1',
        )
        self.user.save()

        self.customer_profile = UserProfile.objects.update(
            default_phone_number='67373',
            default_country='IE',
        )

    def test_is_profile_created(self):
        """
        Test case to check if a customer profile is created and contains the expected values.
        """
        customer_profile = UserProfile.objects.filter().last()
        self.assertEqual(customer_profile.user.username, 'TestName')
        self.assertEqual(customer_profile.default_phone_number, '67373')

    def test_string_method_return(self):
        """
        Test case to check if the string method of UserProfile returns the expected username.
        """
        customer_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(str(customer_profile), 'TestName')
