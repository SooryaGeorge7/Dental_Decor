from django import forms
from reviews.models import Review


class RatingForm(forms.ModelForm):
    """
    Form to edit and delete reviews
    """
    class Meta:
        """
        Define model,  form fields, widgets, labels and help texts.
        """
        model = Review
        fields = [
            'product_rating',
            'comment_text',
            ]
        widgets = {
            
            'comment_text': forms.Textarea(
                attrs={'placeholder': 'Type in a review here...',
                       'class': 'responsive-textarea',
                       }
            ),
        }
        labels = {
            'product_rating': 'Product Rating',
            'comment_text': 'Review Comment',
        }
        help_texts = {
            'comment_text': 'Maximum 500 characters',
        }