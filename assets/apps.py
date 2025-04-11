from django.apps import AppConfig


class AssetsConfig(AppConfig):
    """
    Configuration class for the 'assets' app.
    Registers the app with Django and sets the default primary key type.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'assets'
