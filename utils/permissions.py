"""
Permission utility functions for checking user roles based on group membership.
Used across views to determine access level for different user types.
"""


def is_viewer(user):
    """Check if the user belongs to the 'Viewer' group."""
    return user.groups.filter(name="Viewer").exists()


def is_technician(user):
    """Check if the user belongs to the 'Technician' group."""
    return user.groups.filter(name="Technician").exists()


def is_manager(user):
    """Check if the user belongs to the 'Manager' group."""
    return user.groups.filter(name="Manager").exists()


def is_admin(user):
    """
    Check if the user belongs to the 'Admin' group or is a superuser.
    Superusers automatically get admin access.
    """
    return user.groups.filter(name="Admin").exists() or user.is_superuser
