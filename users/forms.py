from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationFormWithRole(UserCreationForm):
    """
    Custom user creation form that includes role assignment.

    This form adds a dropdown for selecting the user’s group
    (Viewer, Technician, Manager, Admin) during account creation.
    """
    ROLE_CHOICES = [
        ('Viewer', 'Viewer'),
        ('Technician', 'Technician'),
        ('Manager', 'Manager'),
        ('Admin', 'Admin'),
    ]

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        label='User Role',
        help_text='Select a group to assign this user to.'
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']
