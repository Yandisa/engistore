from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User
from inventory.models import Part


class Asset(models.Model):
    """
    Represents a machine, equipment, or system that parts are used on.
    """
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class PartUsage(models.Model):
    """
    Records the usage of a part on a specific asset.
    Links to a user, asset, and part, while validating stock levels.
    """
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    part = models.ForeignKey(Part, on_delete=models.CASCADE)
    quantity_used = models.PositiveIntegerField()
    used_on = models.DateField(auto_now_add=True)
    taken_by = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True
    )

    def __str__(self):
        user_display = self.taken_by.username if self.taken_by else "Unknown"
        return (
            f"{self.part.name} used on {self.asset.name} "
            f"({self.quantity_used}) by {user_display}"
        )

    def clean(self):
        """
        Validates that quantity used does not exceed available stock.
        Only applies on creation (no PK yet).
        """
        if not self.pk and self.quantity_used > self.part.quantity:
            raise ValidationError(
                f"Not enough stock. Tried to use {self.quantity_used}, "
                f"but only {self.part.quantity} available."
            )

    def save(self, *args, **kwargs):
        """
        Runs validation and updates the part's stock only on creation.
        """
        self.full_clean()
        if not self.pk:
            self.part.quantity -= self.quantity_used
            self.part.save()
        super().save(*args, **kwargs)
