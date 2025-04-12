from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    AppConfig for the 'users' app.

    Automatically connects post-migrate signal to create default
    user roles/groups when the app is ready.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # Import signal handler to register post-migrate hook
        import users.signals
