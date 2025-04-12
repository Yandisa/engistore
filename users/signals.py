"""
Signal to create default user roles after database migrations.

Ensures that essential Groups ('Admin', 'Manager', etc.) are always
present, allowing consistent role assignment for users.
"""

from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    """
    Create predefined roles/groups if they don't already exist.

    This runs automatically after every migration.
    """
    default_roles = ['Admin', 'Manager', 'Technician', 'Viewer']
    for role in default_roles:
        Group.objects.get_or_create(name=role)
