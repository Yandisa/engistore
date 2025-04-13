from django import forms
from .models import PartUsage
from inventory.models import Part


class PartUsageForm(forms.ModelForm):
    """
    A form for logging part usage on an asset.

    Includes:
    - Selected part used
    - Quantity taken from inventory

    The associated asset and user are assigned in the view.
    """

    class Meta:
        model = PartUsage
        fields = ['part', 'quantity_used']
        widgets = {
            'part': forms.Select(attrs={
                'class': 'form-select'
            }),
            'quantity_used': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
        }
