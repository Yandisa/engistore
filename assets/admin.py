from django.contrib import admin
from .models import Asset, PartUsage


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    """
    Admin interface customization for the Asset model.

    Displays asset name and code in the list view.
    Enables search functionality by name and code.
    """
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(PartUsage)
class PartUsageAdmin(admin.ModelAdmin):
    """
    Admin interface for tracking part usage.

    Shows the part, asset, quantity used, and usage date.
    Enables filtering by date and asset, and searching by name.
    """
    list_display = ('part', 'asset', 'quantity_used', 'used_on')
    list_filter = ('used_on', 'asset')
    search_fields = ('part__name', 'asset__name')
