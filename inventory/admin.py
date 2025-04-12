from django.contrib import admin
from .models import Part, Category, PartRequest


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Part objects.

    Displays inventory details such as part number, location,
    quantity, and reorder threshold. Enables search by part info.
    """
    list_display = (
        'part_number', 'name', 'category', 'room',
        'aisle', 'bin_number', 'quantity', 'reorder_threshold'
    )
    search_fields = (
        'part_number', 'name', 'room',
        'aisle', 'bin_number'
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Category objects.

    Displays all available part categories.
    """
    list_display = ('name',)


@admin.register(PartRequest)
class PartRequestAdmin(admin.ModelAdmin):
    """
    Admin interface for managing PartRequest objects.

    Displays part request details and allows filtering
    by status and requester. Useful for processing approvals.
    """
    list_display = (
        'name', 'part_number', 'requested_by',
        'status', 'created_at'
    )
    list_filter = ('status',)
    search_fields = (
        'name', 'part_number', 'requested_by__username'
    )
