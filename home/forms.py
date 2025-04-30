from django import forms


class TableSelectionForm(forms.Form):
    TABLE_CHOICES = [
        ('pre-m', 'Pre-meeting'),
        ('post-m', 'Post-meeting'),
        ('dgkh', 'DGKH'),
        ('gal', 'GAL'),
        ('wctl', 'WCTL'),
        ('trgp', 'TRGP'),
    ]
    table = forms.ChoiceField(choices=TABLE_CHOICES, label="Select Company")