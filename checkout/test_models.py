from django.test import TestCase
from .models import Order

class OrderModelTest(TestCase):

    def test_order_model_fields(self):
        """
        Test case to ensure that the fields of the Order model are correctly saved and retrieved.
        """
        order = Order.objects.create(
            full_name='Soorya George',
            email='Soorya@example.com',
            phone_number='1234357890',
            street_address1='665 John St',
            street_address2='Apt 7',
            town_or_city='Wexford',
            postcode='53953',
            country='IE',
            county='Wexford'
        )

        self.assertEqual(order.full_name, 'Soorya George')
        self.assertEqual(order.email, 'Soorya@example.com')
        self.assertEqual(order.phone_number, '1234357890')
        self.assertEqual(order.street_address1, '665 John St')
        self.assertEqual(order.street_address2, 'Apt 7')
        self.assertEqual(order.town_or_city, 'Wexford')
        self.assertEqual(order.postcode, '53953')
        self.assertEqual(order.country, 'IE')
        self.assertEqual(order.county, 'Wexford')
