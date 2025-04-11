from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreationFormWithRole(UserCreationForm):
    """
    Custom user creation form that includes a role selection.
    Users will be assigned to a group (role) upon creation.
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
        help_text='Select the role this user should be assigned to.'
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'role']
