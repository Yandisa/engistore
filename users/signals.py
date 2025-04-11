from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import Group


@receiver(post_migrate)
def create_default_roles(sender, **kwargs):
    roles = ['Admin', 'Manager', 'Technician', 'Viewer']
    for role in roles:
        Group.objects.get_or_create(name=role)
