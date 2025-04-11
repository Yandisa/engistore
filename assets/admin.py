from django.contrib import admin
from .models import Asset, PartUsage


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    """
    Admin interface customization for Asset model.
    Displays name and code in the admin list view.
    """
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


@admin.register(PartUsage)
class PartUsageAdmin(admin.ModelAdmin):
    """
    Admin interface for tracking part usage.
    Shows related part, asset, quantity used, and date.
    Provides filtering and searching capabilities.
    """
    list_display = ('part', 'asset', 'quantity_used', 'used_on')
    list_filter = ('used_on', 'asset')
    search_fields = ('part__name', 'asset__name')
