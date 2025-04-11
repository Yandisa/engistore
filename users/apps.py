from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    AppConfig for the 'users' app.
    Connects signal to create default roles after migrations.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        import users.signals  # ✅ This registers the safe post-migrate signal
