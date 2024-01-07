from django.test import TestCase
from .forms import ProductForm
from .widgets import CustomClearableFileInput
from .models import Category, Product
from django.core.files.uploadedfile import SimpleUploadedFile


class ProductFormTest(TestCase):
    """
    Test for the ProductForm class.
    """
    def setUp(self):
        self.category = Category.objects.create(name='Test Category')

    def test_product_form_invalid_missing_required_fields(self):
        """
        Test case to check if the form is invalid when required fields are missing.
        """
        form = ProductForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors)
        self.assertIn('description', form.errors)
        self.assertIn('price', form.errors)

    def test_product_form_image_field_widget(self):
        """
        Test case to check that the 'image' field uses the expected widget type.
        """
        form = ProductForm()
        self.assertIsInstance(form.fields['image'].widget, CustomClearableFileInput)

    def test_product_form_category_choices(self):
        """
        Test case to check that the 'category' field choices match the expected choices.
        """
        form = ProductForm()
        expected_choices = [(self.category.id, None)]
        self.assertEqual(form.fields['category'].choices, expected_choices)

    def test_product_form_field_widget_classes(self):
        """
        Test case to check that the widget classes of form fields match the expected classes.
        """
        form = ProductForm()
        expected_classes = 'border-dark rounded-0'
        for field_name, field in form.fields.items():
            self.assertEqual(field.widget.attrs['class'], expected_classes)
