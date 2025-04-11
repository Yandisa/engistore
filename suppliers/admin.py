from django.contrib import admin
from .models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Supplier objects.
    Displays name, contact email, and phone in the list view.
    """
    list_display = ('name', 'contact_email', 'phone')
    search_fields = ('name',)
