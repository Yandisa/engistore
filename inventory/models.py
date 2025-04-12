from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    Represents a category for parts
    (e.g., Electrical, Mechanical, Plumbing).
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Part(models.Model):
    """
    Represents a part in the inventory system.

    Includes location breakdown (room, aisle, bin),
    stock levels, and reorder thresholds.
    """
    name = models.CharField(max_length=200)
    part_number = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    description = models.TextField(blank=True)

    # Physical location in store
    room = models.CharField(max_length=50)
    aisle = models.CharField(max_length=50)
    bin_number = models.CharField(max_length=50)

    # Inventory tracking
    quantity = models.PositiveIntegerField(default=0)
    reorder_threshold = models.PositiveIntegerField(default=5)

    # Audit
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.part_number} - {self.name}"


class PartRequest(models.Model):
    """
    A user-submitted request for a part not currently available.

    Used when technicians or viewers request missing stock.
    Status tracks the multi-step approval & fulfillment flow.
    """
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Approved - Awaiting Delivery', 'Approved - Awaiting Delivery'),
        ('Rejected', 'Rejected'),
        ('Delivered', 'Delivered'),
    ]

    # Request details
    name = models.CharField(max_length=200)
    part_number = models.CharField(max_length=100, blank=True)
    quantity_needed = models.PositiveIntegerField()
    reason = models.TextField(blank=True)

    # Meta
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    reviewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Requested by {self.requested_by})"
