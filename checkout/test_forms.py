from django.test import TestCase
from .forms import OrderForm

class OrderFormTest(TestCase):

    def test_order_form_fields(self):
        """
        Test case to ensure that the expected fields are present in the OrderForm.
        """
        form = OrderForm()
        expected_fields = [
            'full_name', 'email', 'phone_number',
            'street_address1', 'street_address2',
            'town_or_city', 'postcode', 'country', 'county',
        ]
        for field in expected_fields:
            self.assertIn(field, form.fields)

    def test_order_form_widget_attrs(self):
        """
        Test case to ensure that the widget attributes of the OrderForm fields are as expected.
        """
        form = OrderForm()
        expected_attrs = {
            'full_name': 'stripe-style-input',
            'email': 'stripe-style-input',
            'phone_number': 'stripe-style-input',
            'street_address1': 'stripe-style-input',
            'street_address2': 'stripe-style-input',
            'town_or_city': 'stripe-style-input',
            'postcode': 'stripe-style-input',
            'country': 'stripe-style-input',
            'county': 'stripe-style-input',
        }
        for field, expected_attr in expected_attrs.items():
            self.assertEqual(form.fields[field].widget.attrs['class'], expected_attr)

    def test_order_form_placeholder(self):
        """
        Test case to ensure that the placeholder attributes of the OrderForm fields are as expected.
        """
        form = OrderForm()
        expected_placeholders = {
            'full_name': 'Full Name *',
            'email': 'Email Address *',
            'phone_number': 'Phone Number *',
            'street_address1': 'Street Address 1 *',
            'street_address2': 'Street Address 2',
            'town_or_city': 'Town or City *',
            'postcode': 'Postal Code',
            'county': 'County, State or Locality',
        }
        for field, expected_placeholder in expected_placeholders.items():
            self.assertEqual(form.fields[field].widget.attrs['placeholder'], expected_placeholder)
