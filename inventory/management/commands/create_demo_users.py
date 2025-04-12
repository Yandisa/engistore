from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group


class Command(BaseCommand):
    help = (
        "Creates or resets demo users with consistent credentials.\n"
        "Useful for testing roles like Admin and Technician."
    )

    def handle(self, *args, **options):
        # Define required user groups
        group_names = ['Admin', 'Manager', 'Technician', 'Viewer']
        for name in group_names:
            Group.objects.get_or_create(name=name)

        # Define demo users
        demo_users = [
            {
                'username': 'admin_demo',
                'password': 'Demo123!',
                'groups': ['Admin']
            },
            {
                'username': 'tech_demo',
                'password': 'Demo123!',
                'groups': ['Technician']
            }
        ]

        # Create or update each demo user
        for user_data in demo_users:
            user, created = User.objects.update_or_create(
                username=user_data['username'],
                defaults={'is_active': True}
            )
            user.set_password(user_data['password'])
            user.save()

            # Clear previous groups and reassign
            user.groups.clear()
            for group_name in user_data['groups']:
                group = Group.objects.get(name=group_name)
                user.groups.add(group)

            action = "✅ Created" if created else "🔁 Updated"
            self.stdout.write(f"{action} user: {user.username}")

        # Summary output
        self.stdout.write("\n🎉 Demo users ready to use:")
        self.stdout.write("👤 Admin: admin_demo / Demo123!")
        self.stdout.write("👷 Technician: tech_demo / Demo123!")
