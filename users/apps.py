from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    AppConfig for the 'users' app.
    Ensures default user roles (groups) are created at startup.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        """
        This method is run when the app is ready.
        It ensures predefined user roles (groups) exist.
        """
        from django.contrib.auth.models import Group

        default_roles = ['Admin', 'Manager', 'Technician', 'Viewer']
        for role in default_roles:
            Group.objects.get_or_create(name=role)
