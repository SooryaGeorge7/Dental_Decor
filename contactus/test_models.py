from django.test import TestCase
from .models import Contact
from django.utils import timezone

class ContactModelTest(TestCase):

    def test_contact_model_creation(self):
        contact = Contact.objects.create(
            name='Soorya George',
            email='soorya@example.com',
            phone='1237777890',
            message='Hello'
        )
        self.assertIsInstance(contact, Contact)
        self.assertEqual(contact.name, 'Soorya George')
        self.assertEqual(contact.email, 'soorya@example.com')
        self.assertEqual(contact.phone, '1237777890')
        self.assertEqual(contact.message, 'Hello')

    def test_contact_model_str_method(self):
        contact = Contact.objects.create(name='Soorya George')
        self.assertEqual(str(contact), "Soorya George's Contact message")

    def test_contact_model_sent_time_auto_now_add(self):
        contact = Contact.objects.create(
            name='Soorya George',
            email='soorya@example.com',
            phone='1237777890',
            message='Hello'
        )
        self.assertIsNotNone(contact.sent_time)
        self.assertLessEqual(contact.sent_time, timezone.now())

    def test_contact_model_ordering(self):
        contact1 = Contact.objects.create(name='Contact 1')
        contact2 = Contact.objects.create(name='Contact 2')
        contacts = Contact.objects.all()
        self.assertEqual(contacts[0], contact2)
        self.assertEqual(contacts[1], contact1)
