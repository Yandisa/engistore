from django.apps import AppConfig


class SuppliersConfig(AppConfig):
    """
    Configuration for the Suppliers app.
    Sets default primary key field type and app name.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'suppliers'
