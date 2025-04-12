"""
Permission utility functions for checking user roles based on group membership.

Used across views to enforce access control for different user types such as
Viewer, Technician, Manager, and Admin.
"""


def is_viewer(user):
    """Returns True if the user belongs to the 'Viewer' group."""
    return user.groups.filter(name="Viewer").exists()


def is_technician(user):
    """Returns True if the user belongs to the 'Technician' group."""
    return user.groups.filter(name="Technician").exists()


def is_manager(user):
    """Returns True if the user belongs to the 'Manager' group."""
    return user.groups.filter(name="Manager").exists()


def is_admin(user):
    """
    Returns True if the user belongs to the 'Admin' group or is a superuser.

    Superusers are treated as Admins by default.
    """
    return user.groups.filter(name="Admin").exists() or user.is_superuser
