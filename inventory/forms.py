from django import forms
from .models import PartRequest


class PartRequestForm(forms.ModelForm):
    """
    Form for technicians and viewers to request new parts.

    Includes fields for part name, optional part number,
    quantity requested, and the reason for the request.
    """

    class Meta:
        model = PartRequest
        fields = [
            'part_name',
            'part_number',
            'quantity_requested',
            'reason',
        ]
        widgets = {
            'part_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Hydraulic Pump'
            }),
            'part_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Optional'
            }),
            'quantity_requested': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'reason': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3
            }),
        }
