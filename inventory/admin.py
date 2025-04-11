from django.contrib import admin
from .models import Part, Category, PartRequest


@admin.register(Part)
class PartAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Part objects.
    Displays inventory details and enables search functionality.
    """
    list_display = (
        'part_number', 'name', 'category', 'room',
        'aisle', 'bin_number', 'quantity', 'reorder_threshold'
    )
    search_fields = ('part_number', 'name', 'room', 'aisle', 'bin_number')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Category objects.
    """
    list_display = ('name',)


@admin.register(PartRequest)
class PartRequestAdmin(admin.ModelAdmin):
    """
    Admin interface for managing PartRequest objects.
    Allows filtering and searching by status and requester.
    """
    list_display = (
        'name', 'part_number', 'requested_by',
        'status', 'created_at'
    )
    list_filter = ('status',)
    search_fields = ('name', 'part_number', 'requested_by__username')

    def get_status(self, obj):
        """
        Determines request status dynamically.
        """
        if obj.approved:
            return "Approved"
        elif obj.reviewed:
            return "Rejected"
        return "Pending"

    get_status.short_description = 'Status'
