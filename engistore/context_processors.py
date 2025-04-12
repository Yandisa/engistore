from django.conf import settings


def global_debug(request):
    """
    Makes the DEBUG setting globally available to all templates.

    You can extend this function to include other global context
    variables (e.g., site settings, user roles, or feature flags).
    """
    return {
        'debug': settings.DEBUG,
    }
