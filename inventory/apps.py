from django.apps import AppConfig


class InventoryConfig(AppConfig):
    """
    Configuration for the Inventory app.
    Sets the default auto field and registers the app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'inventory'
