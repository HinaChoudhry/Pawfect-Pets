from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'comment',
                  )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders for the review form
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'title': 'Title',
            'comment': 'Comment',
        }

        # Add placeholders and classes to input fields

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
