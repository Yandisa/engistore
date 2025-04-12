from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = (
        "Creates test users and assigns them to roles.\n"
        "Use for development or local testing."
    )

    def handle(self, *args, **kwargs):
        users = [
            ('admin_test', 'admin123', 'Admin'),
            ('manager_test', 'manager123', 'Manager'),
            ('technician_test', 'tech123', 'Technician'),
        ]

        for username, password, role in users:
            if User.objects.filter(username=username).exists():
                self.stdout.write(f"🔁 User already exists: {username}")
                continue

            # Create user and assign group
            user = User.objects.create_user(
                username=username,
                password=password
            )
            group, _ = Group.objects.get_or_create(name=role)
            user.groups.add(group)

            if role == "Admin":
                user.is_staff = True
                user.is_superuser = True

            user.save()
            self.stdout.write(
                self.style.SUCCESS(
                    f"✅ Created user: {username} ({role})"
                )
            )
