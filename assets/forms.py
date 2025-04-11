from django import forms
from .models import PartUsage


class PartUsageForm(forms.ModelForm):
    """
    A form for logging part usage.
    Only captures the quantity used.
    The associated part is assigned in the view.
    """

    class Meta:
        model = PartUsage
        fields = ['quantity_used']
        widgets = {
            'quantity_used': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1
            }),
        }
