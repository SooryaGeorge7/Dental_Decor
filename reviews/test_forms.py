from django.test import TestCase
from reviews.models import Review
from .forms import RatingForm
from django import forms

class RatingFormTest(TestCase):

    def test_rating_form_fields(self):
        form = RatingForm()
        expected_fields = ['product_rating', 'comment_text']
        for field in expected_fields:
            self.assertIn(field, form.fields)

    def test_rating_form_widget_attributes(self):
        form = RatingForm()
        self.assertIsInstance(form.fields['product_rating'].widget, forms.HiddenInput)
        self.assertIsInstance(form.fields['comment_text'].widget, forms.Textarea)
        self.assertEqual(
            form.fields['comment_text'].widget.attrs['class'],
            'responsive-textarea'
        )

    def test_rating_form_labels(self):
        form = RatingForm()
        expected_labels = {
            'product_rating': 'Product Rating',
            'comment_text': 'Review Comment',
        }
        for field, expected_label in expected_labels.items():
            self.assertEqual(form.fields[field].label, expected_label)

    def test_rating_form_help_texts(self):
        form = RatingForm()
        expected_help_texts = {
            'comment_text': 'Maximum 500 characters',
        }
        for field, expected_help_text in expected_help_texts.items():
            self.assertEqual(form.fields[field].help_text, expected_help_text)

