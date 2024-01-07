from django import forms
from .models import Contact
import re


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
            'phone': forms.TextInput(attrs={'pattern': r'^\+?[0-9]+$',
                                            'title': 'Enter a valid phone number.'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone',
            'message': 'Message',
        }

   
